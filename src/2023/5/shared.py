def read(file_to_use) -> list[str]:
    with open(file_to_use, 'r') as _:
        return list(map(lambda x: x.replace('\n', '').replace('\r', ''), _.readlines()))


class Transform:
    source_start: int
    source_end: int
    destination_start: int
    destination_end: int

    modifier: int

    def __init__(self, destination_start: int, source_start: int, transform_range: int):
        self.source_start = source_start
        self.source_end = source_start + transform_range - 1
        self.destination_start = destination_start
        self.destination_end = destination_start + transform_range - 1

        self.modifier = destination_start - source_start

    def applies_to(self, value: int, reverse=False) -> bool:
        if reverse:
            return self.destination_start <= value <= self.destination_end
        else:
            return self.source_start <= value <= self.source_end

    def transform(self, value: int):
        """Apply transform. If the input is not inside the source range, it is returned instead."""
        if self.applies_to(value):
            return value + self.modifier
        return value

    def reverse_transform(self, value: int):
        """Apply reverse transform. If the input is outside the destination range, None is returned."""
        if self.applies_to(value, reverse=True):
            return value - self.modifier
        return None

    def __repr__(self):
        symbol = '+' if self.modifier >= 0 else ''
        return f'Transform({self.source_start} to {self.source_end} -> {self.destination_start} to {self.destination_end} [{symbol}{self.modifier}])'


class Almanac:
    SEEDS_KEY = 'seeds'
    SEED_TO_SOIL = 'seed-to-soil map'
    SOIL_TO_FERTILIZER = 'soil-to-fertilizer map'
    FERTILIZER_TO_WATER = 'fertilizer-to-water map'
    WATER_TO_LIGHT = 'water-to-light map'
    LIGHT_TO_TEMP = 'light-to-temperature map'
    TEMP_TO_HUMID = 'temperature-to-humidity map'
    HUMID_TO_LOC = 'humidity-to-location map'

    seeds: list[int] = []
    seed_ranges: list[list[int]] = []
    transforms = {
        SEED_TO_SOIL: [],
        SOIL_TO_FERTILIZER: [],
        FERTILIZER_TO_WATER: [],
        WATER_TO_LIGHT: [],
        LIGHT_TO_TEMP: [],
        TEMP_TO_HUMID: [],
        HUMID_TO_LOC: [],
    }

    def get_transform_set(self, key: str) -> list[Transform]:
        if key in self.transforms:
            return self.transforms[key]
        return []


def build_almanac(lines: list[str], isPartOne=True) -> Almanac:
    _ = Almanac()
    mode = Almanac.SEED_TO_SOIL
    for line in lines:
        if line == '':
            continue

        if line.startswith(Almanac.SEEDS_KEY):
            if isPartOne:
                _.seeds = [int(_) for _ in line.split(': ')[1].split(' ')]
            else:
                _vals = [int(_) for _ in line.split(': ')[1].split(' ')]
                for idx in range(0, len(_vals) - 1, 2):
                    _.seed_ranges.append([_vals[idx], _vals[idx] + _vals[idx + 1] - 1], )
            continue

        _used = False
        for _md in [Almanac.SEED_TO_SOIL, Almanac.SOIL_TO_FERTILIZER,
                    Almanac.FERTILIZER_TO_WATER, Almanac.WATER_TO_LIGHT,
                    Almanac.LIGHT_TO_TEMP, Almanac.TEMP_TO_HUMID,
                    Almanac.HUMID_TO_LOC]:
            if line.startswith(_md):
                _used = True
                mode = _md
                break

        if not _used:
            _values = [int(v) for v in line.split(' ')]
            _.transforms[mode].append(Transform(_values[0], _values[1], _values[2]))
    return _


def transform_seed_to_location(seed: int, with_almanac: Almanac) -> int:
    carry = seed + 0
    for key in with_almanac.transforms:
        for transformer in with_almanac.get_transform_set(key):
            if transformer.applies_to(carry):
                carry = transformer.transform(carry)
                break
    return carry


def transform_location_to_seed(location: int, with_almanac: Almanac, seed_ranges: list) -> int:
    carry = location + 0
    for key in reversed(with_almanac.transforms):
        # Attempt to apply one of the transformers
        applied = False
        for transformer in with_almanac.get_transform_set(key):
            if transformer.applies_to(carry, reverse=True):
                carry = transformer.reverse_transform(carry)
                # print(f'[{location}] -> applying {transformer} -> {carry}')
                applied = True
                break
        # If none were applied, this location cannot be mapped back to a seed
        if not applied:
            return 0
    # check resulting seed against provided seed ranges to see if it is valid
    for _range in seed_ranges:
        print(_range, carry)
        if _range[0] <= carry <= _range[1]:
            return carry
    return 0

def read(file_to_use) -> list[str]:
    with open(file_to_use, 'r') as _:
        return list(map(lambda x: x.replace('\n', '').replace('\r', ''), _.readlines()))


lines = read('input.txt')

SEEDS = 'seeds'
SEED_TO_SOIL = 'seed-to-soil map'
SOIL_TO_FERTILIZER = 'soil-to-fertilizer map'
FERTILIZER_TO_WATER = 'fertilizer-to-water map'
WATER_TO_LIGHT = 'water-to-light map'
LIGHT_TO_TEMP = 'light-to-temperature map'
TEMP_TO_HUMID = 'temperature-to-humidity map'
HUMID_TO_LOC = 'humidity-to-location map'

almanac: dict[str, list] = {
    SEEDS: [],
    SEED_TO_SOIL: [],
    SOIL_TO_FERTILIZER: [],
    FERTILIZER_TO_WATER: [],
    WATER_TO_LIGHT: [],
    LIGHT_TO_TEMP: [],
    TEMP_TO_HUMID: [],
    HUMID_TO_LOC: [],
}

mode = SEED_TO_SOIL

for line in lines:
    if line == '':
        continue

    if line.startswith(SEEDS):
        almanac[SEEDS] = [int(_) for _ in line.split(': ')[1].split(' ')]
        continue

    _used = False
    for _md in [SEED_TO_SOIL, SOIL_TO_FERTILIZER, FERTILIZER_TO_WATER, WATER_TO_LIGHT, LIGHT_TO_TEMP, TEMP_TO_HUMID, HUMID_TO_LOC]:
        if line.startswith(_md):
            _used = True
            mode = _md
            break

    if not _used:
        almanac[mode].append([int(v) for v in line.split(' ')],)


# [print(a, almanac[a]) for a in almanac]

seed_almanacs = []
for seed in almanac[SEEDS]:
    seed_info = {
        'seed': seed
    }

    carry = seed + 0
    for category in almanac:
        if category == SEEDS:
            continue

        for mapping in almanac[category]:
            dest, src, width = mapping
            if src+width >= carry >= src:
                offset = carry - src
                seed_info[category] = dest + offset
                carry = seed_info[category]
                break

        if category not in seed_info:
            seed_info[category] = carry

    seed_almanacs.append(seed_info)

smallest = seed_almanacs[0]
for _ in seed_almanacs:
    if _[HUMID_TO_LOC] < smallest[HUMID_TO_LOC]:
        smallest = _

print('part1: ', smallest[HUMID_TO_LOC])

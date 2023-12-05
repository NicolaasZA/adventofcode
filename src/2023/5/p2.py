from shared import read, build_almanac, transform_location_to_seed, Almanac, transform_seed_to_location

almanac = build_almanac(read('input.txt'), isPartOne=False)

STEP = 10000

smallest = (99999999999, 0)

# Approximate using steps
for seed_range in almanac.seed_ranges:
    _perc = (seed_range[1]-seed_range[0]) / 100
    print(f'looking at {seed_range} with percentage of {_perc} and step of {STEP}')
    for seed in range(seed_range[0], seed_range[1], STEP):
        location = transform_seed_to_location(seed, almanac)
        if location <= smallest[0]:
            smallest = (location, seed)

print(f'Approximate: {smallest[0]} from seed={smallest[1]}')

# Find the exact value within the STEP radius
for seed in range(smallest[1] - STEP, smallest[1] + STEP):
    location = transform_seed_to_location(seed, almanac)
    if location <= smallest[0]:
        smallest = (location, seed)


print(f'Exact: {smallest[0]} from seed={smallest[1]}')

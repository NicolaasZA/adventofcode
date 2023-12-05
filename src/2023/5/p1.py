from shared import read, build_almanac, transform_seed_to_location

almanac = build_almanac(read('demo-input.txt'))

smallest = (99999999999, 0)
for seed in almanac.seeds:
    location = transform_seed_to_location(seed, almanac)
    if location <= smallest[0]:
        smallest = (location, seed)


print(f'part1: {smallest[0]} from seed={smallest[1]}')

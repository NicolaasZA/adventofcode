import math

from shared import find_start, determine_start_type, determine_start_beam, energize, clean

grid = [[x for x in row.strip()] for row in open('input.txt').readlines()]

start_x, start_y = find_start(grid)
start_type = determine_start_type(grid, start_x, start_y)
start_beam = determine_start_beam(start_type, start_x, start_y)

grid[start_y][start_x] = start_type

# We find the loop by shooting a singular beam through it.
# We can discard all pipes and dirt not energized by this beam.
heatmap, max_distance = energize(start_beam, grid)
clean(grid, heatmap)

# Uncomment to print the energized loop
# [print(''.join(_)) for _ in grid]

# Additionally, we can assume a round trip is equal to max_distance, so the furthest point is at the halfway mark.
print(math.floor(max_distance / 2))

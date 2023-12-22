
import shared
from shared import find_start, determine_start_type, determine_start_beam, energize, clean, convert_to_cost_map, \
    find_dots, can_path_to

grid = [[x for x in row.strip()] for row in open('input.txt').readlines()]

start_x, start_y = find_start(grid)
start_type = determine_start_type(grid, start_x, start_y)
start_beam = determine_start_beam(start_type, start_x, start_y)

grid[start_y][start_x] = start_type

# We find the loop by shooting a singular beam through it.
# We can discard all pipes and dirt not energized by this beam.
heatmap, max_distance = energize(start_beam, grid)
clean(grid, heatmap)

print('CLEANED')
[print(*_, sep='') for _ in grid]

# Now we expand the joints around the bends to see where the rabid elf can pass through
# First, expand vertically
y = 1
while y < len(grid):
    _blank = [' '] * len(grid[y])
    grid.insert(y, _blank)
    for x in range(0, len(grid[y])):
        connect_up = grid[y - 1][x] in [shared.TILE_UP_DOWN, shared.TILE_DOWN_RIGHT, shared.TILE_DOWN_LEFT]
        connect_down = grid[y + 1][x] in [shared.TILE_UP_DOWN, shared.TILE_UP_RIGHT, shared.TILE_UP_LEFT]
        if connect_up and connect_down:
            grid[y][x] = shared.TILE_UP_DOWN  # 'X'

    y += 2

# Then, expand horizontally
x = 1
while x < len(grid[0]):
    for y in range(0, len(grid)):
        grid[y].insert(x, ' ')
        connect_left = grid[y][x - 1] in [shared.TILE_UP_RIGHT, shared.TILE_DOWN_RIGHT, shared.TILE_LEFT_RIGHT]
        connect_right = grid[y][x + 1] in [shared.TILE_UP_LEFT, shared.TILE_DOWN_LEFT, shared.TILE_LEFT_RIGHT]
        if connect_left and connect_right:
            grid[y][x] = shared.TILE_LEFT_RIGHT  # 'X'

    x += 2

# Before we do, we pad the whole thing, so we can go around it if needed.
for row in grid:
    row.insert(0, ' ')
    row.append(' ')

_blank = [' '] * len(grid[0])
grid.insert(0, _blank)
grid.append(_blank)

# Uncomment to print the expanded loop
print('EXPANDED')
# [print(*_, sep='') for _ in grid]

# Now that we have a traversable grid, we can use pathfinding to try and get at each dot from outside.
# Pipes cannot be crossed, but everything else if fair game.

# Convert to cost map
cost_map = convert_to_cost_map(grid)

# [print(*_, sep='') for _ in cost_map]

dot_locations = find_dots(grid)
count_inside = 0
for x, y in dot_locations:
    if not can_path_to(x, y, cost_map):
        count_inside += 1
    else:
        grid[y][x] = 'x'

print('\nD*')
[print(*_, sep='') for _ in grid]

print(count_inside)  # 589
# ! THIS PROBLEM IS NOT YET SOLVED.
# ! THE PATHFINDING IS BUGGY

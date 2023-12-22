from shared import Beam, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_UP, DIRECTION_LEFT, energize

grid = [[_ for _ in line.strip()] for line in open('input.txt').readlines()]
max_x = len(grid[0]) - 1
max_y = len(grid) - 1

starting_beams: list[Beam] = []
for x in range(0, max_x + 1):
    starting_beams.append(Beam(x, 0, DIRECTION_DOWN))
    starting_beams.append(Beam(x, max_y, DIRECTION_UP))
for y in range(0, max_y + 1):
    starting_beams.append(Beam(0, y, DIRECTION_RIGHT))
    starting_beams.append(Beam(max_x, y, DIRECTION_LEFT))

print(f'{len(starting_beams)} patterns to energize')

highest = 0
for _b in starting_beams:
    print(f'computing {_b.x}, {_b.y} {_b.dir_name()}')
    result = energize(_b, grid)
    total = sum(map(sum, result))
    if total >= highest:
        highest = total
print(highest)

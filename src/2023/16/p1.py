from shared import Beam, DIRECTION_RIGHT, energize

grid = [[_ for _ in line.strip()] for line in open('input.txt').readlines()]

starting_beam = Beam(0, 0, DIRECTION_RIGHT)

result = energize(starting_beam, grid)

total = sum(map(sum, result))
print(total)
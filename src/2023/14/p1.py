from shared import apply_tilt, weigh

grid = [[_ for _ in line.strip()] for line in open('input.txt').readlines()]

tilted = apply_tilt(grid)

print(weigh(tilted))  # 105461



from shared import dig

lines = [line.strip() for line in open('input.txt').readlines()]

steps = []
for line in lines:
    direction, distance, color = line.split(" ")
    steps.append((direction, int(distance)))

area, perimeter = dig(steps)

# Shoelace / Pick
print(area + perimeter // 2 + 1)

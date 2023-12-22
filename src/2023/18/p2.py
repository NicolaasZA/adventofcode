from shared import dig

lines = [line.strip() for line in open('input.txt').readlines()]

steps = []
for line in lines:
    color = line.split(" ")[-1]
    # get the values from the color field instead
    direction = color[-2]
    distance = color[-7:-2]
    steps.append((direction, int(distance, 16)))

area, perimeter = dig(steps, part2=True)

print(area + perimeter // 2 + 1)

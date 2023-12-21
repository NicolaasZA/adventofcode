from shared import get_box_number

N = open('input.txt').read().strip()

steps = N.split(',')

total = 0
for step in steps:
    _h = get_box_number(step)
    total += _h

print(total)

from shared import get_box_number, Lens

N = open('input.txt').read().strip()

steps = N.split(',')

boxes: list[list[Lens]] = [[] for i in range(0, 256)]

for step in steps:
    label = step.replace('-', '') if '-' in step else step.split('=')[0]
    lens_strength = 0 if '-' in step else int(step.split('=')[1])

    lens = Lens(label, lens_strength)
    box_number = get_box_number(label)

    box = boxes[box_number]

    if lens_strength == 0:
        # Let us remove the lens from the box if present
        for idx in range(0, len(box)):
            if box[idx].label == lens.label:
                del box[idx]
                break
    else:
        # If present, we replace the lens
        present = False
        for lens_in_box in box:
            if lens_in_box.label == lens.label:
                lens_in_box.strength = lens.strength
                present = True
                break

        # Otherwise, we add
        if not present:
            box.append(lens)

# for idx in range(0, 256):
#     if len(boxes[idx]) > 0:
#         print(f'Box {idx}:', boxes[idx])

total = 0
for bx in range(0, len(boxes)):
    box = boxes[bx]

    for lx in range(0, len(box)):
        total += ((bx + 1) * (lx + 1) * box[lx].strength)

print(total)

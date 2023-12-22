DIRECTION_MAPPING_PART_1 = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
DIRECTION_MAPPING_PART_2 = {"0": (0, 1), "1": (1, 0), "2": (0, -1), "3": (-1, 0)}


def dig(steps: list, part2=False):
    x = 0
    y = 0
    perimeter = 0
    area = 0
    for direction, distance in steps:
        dy, dx = DIRECTION_MAPPING_PART_2[direction] if part2 else DIRECTION_MAPPING_PART_1[direction]
        dy, dx = dy * distance, dx * distance
        y, x = y + dy, x + dx
        perimeter += distance
        area += x * dy
    return area, perimeter

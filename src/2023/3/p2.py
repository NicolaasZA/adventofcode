def read(file_to_use) -> list[str]:
    lines: list[str] = []
    with open(file_to_use, 'r') as file:
        lines = file.readlines()
    return list(map(lambda x: x.replace('\n', '').replace('\r', ''), lines))


lines = read('input.txt')

DIGITS = '0123456789'
GEAR = '*'

# pad to simplify search algo
text: list[str] = ['.' * (len(lines[0]) + 2)]
text += ['.' + l + '.' for l in lines]
text.append('.' * (len(lines[0]) + 2))


def is_contact(y, x, val) -> tuple[bool, int, int]:
    if val[y][x] == GEAR:
        return True, x, y
    return False, 0, 0


numbers = []
num = ''
contact_at: tuple[bool, int, int] = (False, 0, 0)
for row in range(1, len(text) - 1):
    for col in range(1, len(text[row])):
        char = text[row][col]

        if DIGITS.count(char) > 0:
            num += char

            # Check for contact
            if not contact_at[0]:
                for coords in [
                    (row - 1, col - 1),
                    (row - 1, col),
                    (row - 1, col + 1),
                    (row, col - 1),
                    (row, col + 1),
                    (row + 1, col - 1),
                    (row + 1, col),
                    (row + 1, col + 1),
                ]:
                    ct = is_contact(coords[0], coords[1], text)
                    if ct[0] is True:
                        contact_at = ct

        elif len(num) > 0:
            if contact_at[0] is True:
                numbers.append((int(num), contact_at))
            contact_at = (False, 0, 0)
            num = ''

grouped = {}
for num in numbers:
    if num[1] not in grouped:
        grouped[num[1]] = []
    grouped[num[1]].append(num[0])

total = 0
for coordinate in grouped:
    vals = grouped[coordinate]
    if len(vals) == 2:
        print(vals[0] * vals[1])
        total += (vals[0] * vals[1])

print(f'part 2: {total}')

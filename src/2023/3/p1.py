import re


def read(file_to_use) -> list[str]:
    lines: list[str] = []
    with open(file_to_use, 'r') as file:
        lines = file.readlines()
    return list(map(lambda x: x.replace('\n', '').replace('\r', ''), lines))


lines = read('input.txt')

DIGITS = '0123456789'
SYMBOLS = '@$&-%+#=/*'

# pad to simplify search algo
text: list[str] = ['.' * (len(lines[0]) + 2)]
text += ['.' + l + '.' for l in lines]
text.append('.' * (len(lines[0]) + 2))

# [print(row) for row in text]

numbers = []
num = ''
contact = False
for row in range(1, len(text) - 1):
    for col in range(1, len(text[row])):
        char = text[row][col]
        if DIGITS.count(char) > 0:
            num += char

            # Check for contact
            if not contact:
                tl, tc, tr = text[row - 1][col - 1], text[row - 1][col], text[row - 1][col + 1]
                cl, cr = text[row][col-1], text[row][col+1]
                bl, bc, br = text[row + 1][col - 1], text[row + 1][col], text[row + 1][col + 1]

                for adjacent in [tl, tc, tr, cl, cr, bl, bc, br]:
                    if SYMBOLS.count(adjacent) > 0:
                        contact = True
                        break

        elif len(num) > 0:
            if contact is True:
                numbers.append(int(num))
            contact = False
            num = ''

print(numbers)
print(sum(numbers))

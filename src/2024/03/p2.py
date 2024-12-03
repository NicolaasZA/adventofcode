import re


def read_commands(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()


FIND_COMMANDS_REGEX = re.compile("do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)")

total = 0
command = read_commands("data.txt")
instructions = FIND_COMMANDS_REGEX.findall(command)
enabled = True
for instruction in instructions:
    if instruction == 'do()':
        enabled = True
    elif instruction == "don't()":
        enabled = False
    elif instruction.startswith("mul("):
        if enabled:
            pieces = instruction.replace('mul(', '').replace(')', '').split(',')
            total += int(pieces[0]) * int(pieces[1])

print(total)
# 110561937
# 104083373

import re


def read_commands(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()


# def clean_tuple(t: tuple) -> str:
#     return [_ for _ in t if _][0]


FIND_COMMANDS_REGEX = re.compile("do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)")

count_dont = 0
count_do = 0

total = 0
command = read_commands("data.txt")
instructions = FIND_COMMANDS_REGEX.findall(command)
print(instructions)
enabled = True
for instruction in instructions:
    print(instruction, enabled)
    if instruction == 'do()':
        count_do += 1
        enabled = True
    elif instruction == "don't()":
        count_dont += 1
        enabled = False
    elif instruction.startswith("mul("):
        if enabled:
            pieces = instruction.replace('mul(', '').replace(')', '').split(',')
            total += int(pieces[0]) * int(pieces[1])

print(total)
# 110561937
# 104083373

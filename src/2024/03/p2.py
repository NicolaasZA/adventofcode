import re


def read_commands(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()


FIND_COMMANDS_REGEX = re.compile(r"do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)")

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
            x,y = instruction.replace('mul(', '').replace(')', '').split(',')
            total += int(x) * int(y)

print(total)

import re


def read_commands(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return file.readlines()


total = 0
commands = read_commands("data.txt")
for command in commands:
    instructions = re.findall("mul\(\d{1,3},\d{1,3}\)", command)
    for instruction in instructions:
        pieces = instruction.replace('mul(', '').replace(')', '').split(',')
        total += int(pieces[0]) * int(pieces[1])

print(total)

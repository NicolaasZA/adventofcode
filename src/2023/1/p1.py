import re


def read(file_to_use):
    lines: list[str] = []
    with open(file_to_use, 'r') as file:
        lines = file.readlines()
    return list(map(lambda x: x.replace('\n', '').replace('\r', ''), lines))


def convert_line(line: str) -> int:
    numbers_only = re.sub('[^0-9]+', '', line)
    # if len(numbers_only) == 1:
    #     return int(numbers_only[0] + numbers_only[0])
    return int(numbers_only[0] + numbers_only[-1])


if __name__ == '__main__':
    filtered: list[int] = list(map(lambda x: convert_line(x), read('input.txt')))
    print('part 1:', sum(filtered))

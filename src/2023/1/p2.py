from p1 import read

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def find_number(line: str, rng) -> int:
    padded = line + '               '
    for idx in rng:
        if line[idx] in '123456789':
            return int(line[idx])

        for digit in numbers:
            piece = padded[idx:idx + len(digit)]
            if piece == digit:
                return numbers.index(digit) + 1
    return 0


def get_first(line: str) -> int:
    return find_number(line, range(0, len(line)))


def get_last(line: str) -> int:
    return find_number(line, reversed(range(0, len(line))))


filtered: list[int] = list(map(lambda x: int(f'{get_first(x)}{get_last(x)}'), read('input.txt')))
print('part 2:', sum(filtered))  # 53866

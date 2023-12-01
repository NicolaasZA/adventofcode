import re

from p1 import read, convert_line

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def magic(line: str, rng) -> int:
    padded = line + '               '
    for idx in rng:
        if line[idx] in '123456789':
            return int(line[idx])

        for digit in numbers:
            from_idx, to_idx, replace_with = idx, idx + len(digit), numbers.index(digit) + 1
            piece = padded[from_idx:to_idx]
            if piece == digit:
                return replace_with
    return 0


def get_first(line: str) -> int:
    return magic(line, range(0, len(line)))


def get_last(line: str) -> int:
    return magic(line, reversed(range(0, len(line))))


def convert_line_with_text_numbers(line: str) -> int:
    return int(f'{get_first(line)}{get_last(line)}')


filtered: list[int] = list(map(lambda x: convert_line_with_text_numbers(x), read('input.txt')))
sums = 0
for num in filtered:
    sums += num
print('part 2:', sums)  # 53866

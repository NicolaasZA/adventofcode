from functools import cmp_to_key

from shared import file_to_lines, Hand


def compare(a: Hand, b: Hand) -> int:
    if a.strength > b.strength:
        return 1
    elif a.strength < b.strength:
        return -1
    return a.has_higher_cards_than(b)


lines = file_to_lines('input.txt')

hands = [Hand(line, True) for line in lines]

sorted_hands = list(sorted(hands, key=cmp_to_key(compare)))

total = 0
rank = 1
for _ in sorted_hands:
    total += (_.bid * rank)
    rank += 1

print(f'Part 2: {total}')  # 254412181

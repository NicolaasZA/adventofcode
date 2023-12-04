from p1 import read

cards = read('input.txt')
counters = [1] * len(cards)

__card_count = 0
__carry = 1
for idx in range(0, len(cards)):
    card = cards[idx]
    winning = [_ for _ in card.split('|')[0].split(':')[1].split(' ') if _ != '']
    elf = [_ for _ in card.split('|')[1].split(' ') if _ != '']

    score = 0
    for num in elf:
        if num in winning:
            score += 1

    for v in range(0, counters[idx]):
        for v2 in range(1, score + 1):
            if idx + v2 < len(counters):
                counters[idx + v2] += 1

print(f'part 2: {sum(counters)}')

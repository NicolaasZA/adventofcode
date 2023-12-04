def read(file_to_use) -> list[str]:
    lines: list[str] = []
    with open(file_to_use, 'r') as file:
        lines = file.readlines()
    return list(map(lambda x: x.replace('\n', '').replace('\r', ''), lines))


if __name__ == '__main__':
    cards = read('input.txt')
    tally = 0
    for idx in range(0, len(cards)):
        card = cards[idx]
        winning = [_ for _ in card.split('|')[0].split(':')[1].split(' ') if _ != '']
        elf = [_ for _ in card.split('|')[1].split(' ') if _ != '']

        score = 0
        for num in elf:
            if num in winning:
                score = 1 if score == 0 else score * 2
        tally += score

    # print(counters)
    print(f'part 1: {tally}')

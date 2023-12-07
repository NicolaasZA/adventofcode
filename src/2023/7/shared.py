POSSIBLE_CARDS = ['X', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class Hand:
    _card_counts: dict[str, int]
    bid: int
    strength: int
    rank = 0
    desc: str

    _cards: str

    def __init__(self, hand: str, isPartTwo=False):
        self.bid = int(hand.split(' ')[1])
        self._cards = hand.split(' ')[0]
        self.map_counts(self._cards)
        self.strength = self.get_strength() if not isPartTwo else self.get_strength_p2()

    def map_counts(self, hand: str):
        self._card_counts = {}
        for _ in hand:
            if _ in self._card_counts:
                self._card_counts[_] += 1
            else:
                self._card_counts[_] = 1

    def remap_counts(self):
        self.map_counts(self._cards)

    def get_highest_count(self) -> tuple[str, int]:
        _highest_val = max(self._card_counts.values())
        return [(key, self._card_counts[key]) for key in self._card_counts if self._card_counts[key] == _highest_val][0]

    def has_higher_cards_than(self, other_hand: "Hand"):
        for idx in range(0, len(self._cards)):
            my_card_face = POSSIBLE_CARDS.index(self._cards[idx])
            their_card_face = POSSIBLE_CARDS.index(other_hand._cards[idx])
            if my_card_face > their_card_face:
                return 1
            elif their_card_face > my_card_face:
                return -1
        return 0

    def get_strength(self):
        _card_variety_count = len(self._card_counts.keys())
        if (_card_variety_count == 1) and (5 in self._card_counts.values()):
            # 5 of a kind
            self.desc = '5 of a kind'
            return 6

        if (_card_variety_count == 2) and (4 in self._card_counts.values()) and (1 in self._card_counts.values()):
            # 4 of a kind
            return 5

        if 3 in self._card_counts.values() and 2 in self._card_counts.values():
            # 3 of a kind and 1 pair
            return 4
        elif 3 in self._card_counts.values():
            # 3 of a kind
            return 3

        if (_card_variety_count == 3) and (3 not in self._card_counts.values()):
            # 2 pair
            return 2

        if _card_variety_count == 4:
            # 1 pair
            return 1

        # high card
        return 0

    def get_card_with_count(self, cnt: int):
        first_key: str = ''
        for _ in self._card_counts:
            if first_key == '':
                first_key = _
            if self._card_counts[_] == cnt:
                return _
        return first_key

    def get_highest_card(self):
        highest_idx, highest_card = 0, self.get_card_with_count(99)
        for _ in self._cards:
            if POSSIBLE_CARDS.index(_) > highest_idx:
                highest_idx = POSSIBLE_CARDS.index(_)
                highest_card = _
        return highest_card

    def get_strength_p2(self):
        if 'J' not in self._cards:
            return self.get_strength()

        del self._card_counts['J']
        self._cards = self._cards.replace('J', 'X')

        _card_variety_count = len(self._card_counts.keys())
        _card_count = sum(self._card_counts.values())

        if _card_variety_count == 1 or _card_count == 0:
            # AAAA or AAA or AA or A or nothing
            return 6  # 5 of a kind

        if _card_variety_count == 2:
            if _card_count == 4:
                if 3 in self._card_counts.values():
                    # ABBB or AAAB
                    return 5  # 4 of kind
                else:
                    # AABB
                    return 4  # 3 of kind with pair
            else:
                # AAB or ABB or AB
                return 5  # 4 of a kind

        if _card_variety_count == 3:
            if _card_count == 4:
                # AABC or ABBC or ABCC
                return 3  # 3 of a kind
            else:
                # ABC
                return 3  # 3 of a kind

        if _card_variety_count == 4:
            # ABCD
            return 1  # 1 pair

        return self.get_strength()

    def __repr__(self):
        return f'Hand("{self._cards}", bid={self.bid}, strength={self.strength})'


def file_to_lines(file_path: str) -> list[str]:
    with open(file_path, 'r') as _:
        return list(map(lambda x: x.replace('\n', '').replace('\r', ''), _.readlines()))

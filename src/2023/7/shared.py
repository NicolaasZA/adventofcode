POSSIBLE_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class Hand:
    _card_counts: dict[str, int]
    bid: int
    strength: int
    rank = 0
    desc: str

    _cards: str

    def __init__(self, hand: str):
        self._cards = hand.split(' ')[0]
        self.map_counts(self._cards)
        self.strength = self.get_strength()
        self.bid = int(hand.split(' ')[1])

    def map_counts(self, hand: str):
        self._card_counts = {}
        for _ in hand:
            if _ in self._card_counts:
                self._card_counts[_] += 1
            else:
                self._card_counts[_] = 1

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

    def __repr__(self):
        return f'Hand("{self._cards}", {len(self._card_counts.keys())}, bid={self.bid}, strength={self.strength})'


def file_to_lines(file_path: str) -> list[str]:
    with open(file_path, 'r') as _:
        return list(map(lambda x: x.replace('\n', '').replace('\r', ''), _.readlines()))

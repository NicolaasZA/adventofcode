class Lens:
    label: str
    strength: int

    def __init__(self, label: str, strength: int):
        self.label = label
        self.strength = strength

    def __repr__(self):
        return f'{self.label} {self.strength}'


def get_box_number(label: str):
    _value = 0

    for char in label:
        _value += ord(char)
        _value *= 17
        _value %= 256

    return _value
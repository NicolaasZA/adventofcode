class Mapping:
    name: str
    left: str
    right: str
    end: str

    def __init__(self, line: str):
        super().__init__()
        self.name = line.split('=')[0].strip()
        left, right = line.split('=')[1].split(',')
        self.left = left.replace('(', '').strip()
        self.right = right.replace(')', '').strip()
        self.end = self.name[-1]

    def step(self, step: str):
        if step == 'L':
            return self.left
        return self.right

    def __repr__(self):
        return f'{self.name} = ({self.left}, {self.right})'
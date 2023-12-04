class Action:
    fromStack: int
    toStack: int
    count: int

    def __init__(self, line: str):
        # interpret line
        parts = line.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")

        # assign
        self.count = int(parts[0])
        self.fromStack = int(parts[1]) - 1
        self.toStack = int(parts[2]) - 1

    def __repr__(self) -> str:
        return "Action(move {} from {} to {})".format(self.count, self.fromStack + 1, self.toStack + 1)

    def __str__(self) -> str:
        return self.__repr__()
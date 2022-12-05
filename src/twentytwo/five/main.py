from classes import Action

board = []
actions: list[Action] = []

def readInput(pathToFile: str):
    b = [[],[],[],[],[],[],[],[],[]]
    a = []

    actionMode = False
    lines = []
    with open(pathToFile) as puzzleInput:
        lines = puzzleInput.readlines()
        
    for line in lines:
        if line.startswith(" 1") or line == '\n':
            actionMode = True
        else:
            if actionMode:
                a.append(Action(line))
            else:
                entries = [line[1],line[5],line[9],line[13],line[17],line[21],line[25],line[29],line[33]]
                for i in range(0, len(entries)):
                    if entries[i] != ' ':
                        b[i].insert(0, entries[i])
            

    return b, a

def boardAsString():
    string = ""
    for column in board:
        if len(column) > 0:
            string += column[-1]
    return string


def partOne():
    # execute actions
    for action in actions:
        for iter in range(0, action.count):
            moveItem = board[action.fromStack].pop()
            board[action.toStack].append(moveItem)

    print(boardAsString()) # FCVRLMVQP


def partTwo():
    # execute actions with multi-stack
    for action in actions:
        fromIndex = len(board[action.fromStack]) - action.count
        if fromIndex < 0:
            fromIndex = 0

        moveItems = board[action.fromStack][fromIndex:]
        board[action.fromStack] = board[action.fromStack][:fromIndex]
        board[action.toStack].extend(moveItems)

    print(boardAsString()) # RWLWGJGFD


if __name__ == '__main__':
    board, actions = readInput("./input.txt")
    # partOne()
    partTwo()


sequence = ''

def readInput(pathToFile: str) -> str:
    result = ''
    with open(pathToFile) as fi:
        result = fi.readline()
    return result        


def hasDuplicates(text: str) -> bool:
    for char in text:
        if text.count(char) > 1:
            return True
    return False


def partOne():
    start = 0
    end = 4

    while end < len(sequence):
        piece = sequence[start:end]
        
        if hasDuplicates(piece) == False:
            print('part one answer:', end) # 1140
            return

        start += 1
        end += 1


def partTwo():
    start = 0
    end = 14

    while end < len(sequence):
        piece = sequence[start:end]
        
        if hasDuplicates(piece) == False:
            print('part two answer:', end) # 3495
            return

        start += 1
        end += 1


if __name__ == '__main__':
    sequence = readInput("./input.txt")
    partOne()
    partTwo()
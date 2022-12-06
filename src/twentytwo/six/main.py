

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


def findUnique(txt: str, size: int) -> int:
    start = 0
    end = 0 + size

    while end < len(txt):
        piece = txt[start:end]

        if hasDuplicates(piece) == False:
            return end

        start += 1
        end += 1

    return -1


def partOne():
    print('part one answer:', findUnique(sequence, 4))  # 1140


def partTwo():
    print('part two answer:', findUnique(sequence, 14))  # 3495


if __name__ == '__main__':
    sequence = readInput("./input.txt")
    partOne()
    partTwo()

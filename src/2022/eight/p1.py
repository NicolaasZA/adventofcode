import copy


def readInput(pathToFile: str) -> list[str]:
    result = []
    with open(pathToFile) as fi:
        result = fi.readlines()
    return result


def inputToArrays(inp: list[str]) -> list[list[int]]:
    result = [[0] * len(inp)] * len(inp)

    for iter in range(0, len(inp)):
        inp[iter] = inp[iter].replace("\n", "")
        result[iter] = [int(e) for e in inp[iter]]

    return result


lines = readInput("input.txt")
forest = inputToArrays(lines)
vis_map = copy.deepcopy(forest)

# [print(line) for line in forest]

for row in range(0, len(forest)):
    for col in range(0, len(forest)):
        if (row == 0) or (col == 0) or (row == len(forest)-1) or (col == len(forest)-1):
            #outside layer is always visible
            vis_map[row][col] = 1
        else:
            # check left if visible
            isVisFromLeft = True
            for c in range(0, col):
                if forest[row][c] >= forest[row][col]:
                    isVisFromLeft = False
            
            # check right if visible
            isVisFromRight = True
            for c in range(col+1, len(forest)):
                if forest[row][c] >= forest[row][col]:
                    isVisFromRight = False
            
            # check up if visible
            isVisFromUp = True
            for r in range(0, row):
                if forest[r][col] >= forest[row][col]:
                    isVisFromUp = False
            
            # check down if visible
            isVisFromDown = True
            for r in range(row+1, len(forest)):
                if forest[r][col] >= forest[row][col]:
                    isVisFromDown = False

            # print(row, col, vis_map[row][col], isVisFromLeft, isVisFromRight, isVisFromUp, isVisFromDown)
            vis_map[row][col] = 1 if (isVisFromLeft or isVisFromRight or isVisFromUp or isVisFromDown) else 0
          

# [print(line) for line in vis_map]

tree_count = 0
for line in vis_map:
    tree_count += line.count(1)
print(tree_count)

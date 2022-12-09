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


def count_visible(view_tree: int, trees: list[int]):
    if len(trees) == 0:
        return 0

    count = 0
    for i in range(0, len(trees)):
        # if this tree is as tall as or taller than the viewer height, stop counting, but include this tree
        if trees[i] >= view_tree:
            count += 1
            return count

        # if this tree is shorter than our viewing tree, it is visible
        if (view_tree > trees[i]):
            count += 1

    return count


lines = readInput("input.txt")
forest = inputToArrays(lines)

score = 0
for row in range(0, len(forest)):
    for col in range(0, len(forest[row])):
        trees_up = [forest[r][col] for r in reversed(range(0, row))]
        trees_left = [forest[row][c] for c in reversed(range(0, col))]
        trees_down = [forest[r][col] for r in range(row + 1, len(forest))]
        trees_right = [forest[row][c] for c in range(col+1, len(forest[row]))]

        score_up = count_visible(forest[row][col], trees_up)
        score_left = count_visible(forest[row][col], trees_left)
        score_down = count_visible(forest[row][col], trees_down)
        score_right = count_visible(forest[row][col], trees_right)

        score = max(score, score_up * score_left * score_down * score_right)

print(score)

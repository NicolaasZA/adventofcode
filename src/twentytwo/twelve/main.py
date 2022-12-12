# Breadth-First Search
def bfs(start):
    queue, seen = [[start]], {start}
    while queue:
        path = queue.pop(0)
        i, j = path[-1]
        if maparr[i][j] == "E":
            return path
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            # Prevent out-of-bounds
            if 0 <= x < len(maparr) and 0 <= y < len(maparr[0]):
                if (x, y) not in seen and height_func(maparr[x][y]) - height_func(maparr[i][j]) < 2:
                    queue.append(path + [(x, y)])
                    seen.add((x, y))


def height_func(x):
    if x not in 'SE':
        return ord(x)
    else:
        return ord('a') if x == 'S' else ord('z')


maparr = [list(x.strip()) for x in open('input.txt').readlines()]

for part in ['S', 'aS']:
    # Calculate two paths, one for S to E, one for nearest A
    starts = [(i, j) for j in range(len(maparr[0]))
              for i in range(len(maparr)) if maparr[i][j] in part]
    print(min(len(path) - 1 for s in starts if (path := bfs(s)) is not None))

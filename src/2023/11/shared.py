class Star:
    chart_x: int
    chart_y: int
    x: int
    y: int
    uid: int

    def __init__(self, uid, x, y):
        self.uid = uid
        self.x = x
        self.y = y
        self.chart_x = x + 0
        self.chart_y = y + 0

    def __repr__(self):
        return f'{self.uid} ({self.x}, {self.y}) (was at {self.chart_x}, {self.chart_y})'


def convert(raw: list[list[str]]) -> tuple[list[list[int]], int]:
    chart = []
    uid = 1
    for y in range(0, len(raw)):
        chart.append([])
        for x in range(0, len(raw[y])):
            if raw[y][x] == '#':
                chart[y].append(uid)
                uid += 1
            else:
                chart[y].append(0)
    return chart, uid


def expand(chart: list[list[int]], factor=1) -> list[Star]:
    # im too fucking sleepy to grep why I need this if
    if factor > 1:
        factor -= 1

    # Extract stars
    _stars: list[Star] = []
    for y in range(len(chart)):
        for x in range(len(chart[y])):
            if chart[y][x] > 0:
                _stars.append(Star(chart[y][x], x, y))

    # find horizontal and vertical empty lines
    hor = []
    ver = []

    # Scan horizontally
    for x in range(len(chart[0])):
        has_value = False
        for y in range(0, len(chart)):
            if chart[y][x] > 0:
                has_value = True
        if not has_value:
            hor.append(x)

    # Scan vertically
    for y in range(len(chart)):
        if sum(chart[y]) == 0:
            ver.append(y)

    # Perform expansion
    for star in _stars:
        for x in hor:
            if star.chart_x > x:
                star.x += factor
        for y in ver:
            if star.chart_y > y:
                star.y += factor
    return _stars


def fast_dist(a: Star, b: Star) -> int:
    if a.x == b.x:
        return abs(b.y - a.y)
    elif a.y == b.y:
        return abs(b.x - a.x)

    # walk the parallel portion using fast math
    # This speeds up dist() since it just needs to manually step the last distance if needed
    delta_x = abs(b.x - a.x)
    delta_y = abs(b.y - a.y)
    shortest_side = min(delta_x, delta_y)

    sx, sy = a.x + 0, a.y + 0
    if a.x > b.x:
        sx = a.x - shortest_side
    else:
        sx = a.x + shortest_side

    if a.y > b.y:
        sy = a.y - shortest_side
    else:
        sy = a.y + shortest_side

    return dist(sx, sy, b.x, b.y, shortest_side * 2)


def dist(sx, sy, dx, dy, starting_distance=0):
    if sx == dx:
        return starting_distance + abs(dy - sy)
    elif sy == dy:
        return starting_distance + abs(dx - sx)

    _dist = starting_distance + 0
    wx, wy = sx + 0, sy + 0
    while wx != dx or wy != dy:
        if wx < dx:
            wx += 1
            _dist += 1
        elif wx > dx:
            wx -= 1
            _dist += 1
        if wy < dy:
            wy += 1
            _dist += 1
        elif wy > dy:
            wy -= 1
            _dist += 1
    return _dist

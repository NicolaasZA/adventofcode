from timeit import timeit
import time

DEBUG_ENABLED = False

AIR = 0
AIR_CHAR = '.'

DIRT = 1
DIRT_CHAR = '#'

SAND = 2
SAND_CHAR = 'o'

FLOOR = 1000
FLOOR_CHAR = '='

NOTHING = 999


def debug(*args):
    if DEBUG_ENABLED:
        print(*args)


def read_structure_data(fileName='./input2.txt'):
    lines = []
    with open(fileName, 'r') as fi:
        lines = fi.readlines()
    return list(map(lambda l: l.replace('\n', ''), lines))


class Point:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @staticmethod
    def fromText(txt: str):
        return Point(int(txt.split(",")[0]), int(txt.split(",")[1]))

    def __str__(self) -> str:
        return f'P({self.x},{self.y})'

    def __repr__(self) -> str:
        return self.__str__()

    def clone(self):
        return Point(self.x+0, self.y+0)


class Stage:

    grid: list[list[int]]
    has_floor = False

    def __init__(self):
        self.grid = []
        for y in range(1001):
            self.grid.append(1000 * [0])

    def get(self, x: int, y: int, fill=NOTHING) -> int:
        if x < 0 or y < 0 or x > 1000 or y > 1000:
            return fill
        return self.grid[y][x]

    def set(self, x: int, y: int, val: int):
        self.grid[y][x] = val

    def getCoord(self, coord: Point) -> int:
        return self.get(coord.x, coord.y)

    def setCoord(self, coord, val: int):
        self.set(coord.x, coord.y, val)

    def getRange(self):
        '''Get the square range the data in the stage is contained in.'''
        minx, maxx, miny, maxy = 1000, 0, 1000, 0
        for y, row in enumerate(self.grid, start=0):
            for x, cell in enumerate(row, start=0):
                if cell in (DIRT, SAND):
                    minx = min(minx, x)
                    maxx = max(maxx, x)
                    miny = min(miny, y)
                    maxy = max(maxy, y)

        return minx, maxx, miny, maxy

    def add_floor(self):
        _,_,_,max_y = self.getRange()
        y = max_y +2
        for x in range(0, len(self.grid[y])):
            self.grid[y][x] = FLOOR
        self.has_floor = True


def draw_stage(stage: Stage):
    min_x, max_x, min_y, max_y = stage.getRange()
    min_x -= 1
    max_x += 1
    max_y += 2
    print()

    # HEADER
    hl = '/9'
    for x in range(min_x, max_x + 1):
        hl += str(x % 10)
    print(hl)

    images = [AIR_CHAR, DIRT_CHAR, SAND_CHAR]
    special = [' ', FLOOR_CHAR]
    for y in range(min_y, max_y+1):
        map_line = f'{y%10} '
        for x in range(min_x, max_x+1):
            v = stage.get(x, y)
            if v >= NOTHING:
                map_line += special[v - NOTHING]
            else:
                map_line += images[v]
        print(map_line)
    print()


def build_stage(data: list[str]) -> Stage:
    stage = Stage()
    for line in data:
        steps = line.split(" -> ")
        debug(f'drawing command: {line}')
        for i in range(0, len(steps) - 1):
            from_coords = Point.fromText(steps[i])
            to_coords = Point.fromText(steps[i+1])

            if from_coords.y == to_coords.y:
                y = from_coords.y
                start_x = min(from_coords.x, to_coords.x)
                end_x = max(from_coords.x, to_coords.x)
                for x in range(start_x, end_x+1):
                    stage.set(x, y, DIRT)

            elif from_coords.x == to_coords.x:
                x = from_coords.x
                start_y = min(from_coords.y, to_coords.y)
                end_y = max(from_coords.y, to_coords.y)
                for y in range(start_y, end_y+1):
                    stage.set(x, y, DIRT)
    return stage


def has_point_in_stage(st: list[Point], point: Point):
    for p in st:
        if p.x == point.x and p.y == point.y:
            return True
    return False


def calc_move(s: Stage, p, max_y: int) -> Point | str | None:
    '''Calulcate the next move for a sand particle at Point p. If max_y is reached, overflow is declared.'''
    below = Point(p.x, p.y+1)
    left = Point(p.x-1, p.y+1)
    right = Point(p.x+1, p.y+1)

    if below.y >= max_y and not s.has_floor:
        return 'ERROR'

    if s.getCoord(below) == AIR:
        return below
    elif s.getCoord(left) == AIR:
        return left
    elif s.getCoord(right) == AIR:
        return right

    return None


def simulate_sand(s: Stage, sp: Point) -> int:
    '''Simulate falling path sand, spawning at Point sp. Returns ammount of sand that spawned.'''
    max_y = s.getRange()[3] + 2
    debug(f'simulating... max_y = {max_y}')

    is_overflowing = False

    times = []

    i = 0
    while s.getCoord(sp) == AIR and not is_overflowing:
        start = time.perf_counter()
        sand_location = sp.clone()

        m = 0
        next_location = sand_location
        while next_location is not None:
            next_location = calc_move(s, sand_location, max_y)
            m += 1

            if next_location == 'ERROR':
                time_taken = sum(times, start=0)
                debug(f'{i} sands taking average {time_taken/i}, total {time_taken}')
                return i
            elif next_location is not None:
                sand_location = next_location

        s.setCoord(sand_location, SAND)

        end = time.perf_counter()
        times.append(end-start)
        # print(f'sand {i} took {m} moves taking {end-start}')
        i += 1

    time_taken = sum(times, start=0)
    debug(f'{i} sands taking average {time_taken/i}, total {time_taken}')
    return i


def part_one(input_file: str):
    struct_data = read_structure_data(input_file)

    stage = build_stage(struct_data)
    # draw_stage(stage)

    # stage.add_floor()

    count = simulate_sand(stage, Point(500, 0))
    # draw_stage(stage)

    print(count)

def part_two(input_file: str):
    struct_data = read_structure_data(input_file)

    stage = build_stage(struct_data)
    # draw_stage(stage)

    stage.add_floor()

    count = simulate_sand(stage, Point(500, 0))
    # draw_stage(stage)

    print(count)


if __name__ == '__main__':
    part_one('./input.txt')
    part_two('./input.txt')

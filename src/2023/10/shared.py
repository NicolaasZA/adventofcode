import math
from copy import deepcopy

import numpy as np
import tcod.path as tpath

DIRECTION_RIGHT = 0
DIRECTION_UP = 1
DIRECTION_LEFT = 2
DIRECTION_DOWN = 3

TILE_GROUND = '.'
TILE_UP_DOWN = '|'
TILE_LEFT_RIGHT = '-'
TILE_UP_RIGHT = 'L'
TILE_UP_LEFT = 'J'
TILE_DOWN_LEFT = '7'
TILE_DOWN_RIGHT = 'F'
TILE_FILLER = 'X'

PIPES = [
    TILE_UP_DOWN,
    TILE_LEFT_RIGHT,
    TILE_UP_RIGHT,
    TILE_UP_LEFT,
    TILE_DOWN_LEFT,
    TILE_DOWN_RIGHT,
    TILE_FILLER
]


class Beam:
    history: list
    x: int
    y: int
    uid: int

    direction: int
    distance: int

    def __init__(self, x: int, y: int, direction: int, history: list = None):
        self.history = history if history is not None else []
        self.x = x
        self.y = y
        self.distance = 0
        self.direction = direction

    def duplicate(self):
        return Beam(self.x + 0, self.y + 0, self.direction + 0, history=deepcopy(self.history))

    def dir_name(self):
        return ['right', 'up', 'left', 'down'][self.direction]

    def log(self):
        self.history.append([self.x + 0, self.y + 0, self.direction])

    def move_one(self):
        if self.direction == DIRECTION_RIGHT:
            self.x += 1
        elif self.direction == DIRECTION_UP:
            self.y -= 1
        elif self.direction == DIRECTION_LEFT:
            self.x -= 1
        else:
            self.y += 1
        self.distance += 1

    def is_at(self, x, y):
        return self.x == x and self.y == y

    def __repr__(self):
        return f'Beam at {self.x}, {self.y} going {self.dir_name()}'


def add_beam(others: list[Beam], to_add: Beam):
    match = False
    for b in others:
        if b.x == to_add.x and b.y == to_add.y and b.direction == to_add.direction:
            match = True
            break
        elif [to_add.x, to_add.y, to_add.direction] in b.history:
            match = True
            break

    if not match:
        others.append(to_add)


def energize(beam: Beam, grid: list[list[str]], heatmap=True):
    energy_grid = deepcopy(grid)
    for y in range(0, len(energy_grid)):
        for x in range(0, len(energy_grid[y])):
            energy_grid[y][x] = 0

    start_x, start_y = beam.x + 0, beam.y + 0
    max_x, max_y = len(grid[0]), len(grid)

    # simulate until all the beams leave the grid
    while (max_x > beam.x >= 0) and (max_y > beam.y >= 0) and not (beam.is_at(start_x, start_y) and beam.history != []):
        # beam must be in the grid
        # beam must be in a pipe
        # if beam reaches the start point, we are done
        beam_tile = grid[beam.y][beam.x]
        # print(f'beam is at {beam.x}, {beam.y} on {beam_tile} going {beam.dir_name()}')
        beam.log()
        energy_grid[beam.y][beam.x] = 1 if heatmap else beam.distance

        # decide action based on tile
        if beam.is_at(start_x, start_y):
            beam.move_one()
        elif beam_tile == TILE_UP_DOWN:
            if beam.direction in [DIRECTION_UP, DIRECTION_DOWN]:
                beam.move_one()
            else:
                # Pipe connection no good. Die.
                break
        elif beam_tile == TILE_LEFT_RIGHT:
            if beam.direction in [DIRECTION_LEFT, DIRECTION_RIGHT]:
                beam.move_one()
            else:
                # Pipe connection no good. Die.
                break
        elif beam_tile == TILE_UP_RIGHT:
            if beam.direction == DIRECTION_LEFT:
                beam.direction = DIRECTION_UP
                beam.move_one()
            elif beam.direction == DIRECTION_DOWN:
                beam.direction = DIRECTION_RIGHT
                beam.move_one()
            else:
                # Pipe connection no good. Die.
                break
        elif beam_tile == TILE_UP_LEFT:
            if beam.direction == DIRECTION_RIGHT:
                beam.direction = DIRECTION_UP
                beam.move_one()
            elif beam.direction == DIRECTION_DOWN:
                beam.direction = DIRECTION_LEFT
                beam.move_one()
            else:
                # Pipe connection no good. Die.
                break
        elif beam_tile == TILE_DOWN_LEFT:
            if beam.direction == DIRECTION_RIGHT:
                beam.direction = DIRECTION_DOWN
                beam.move_one()
            elif beam.direction == DIRECTION_UP:
                beam.direction = DIRECTION_LEFT
                beam.move_one()
            else:
                # Pipe connection no good. Die.
                break
        elif beam_tile == TILE_DOWN_RIGHT:
            if beam.direction == DIRECTION_LEFT:
                beam.direction = DIRECTION_DOWN
                beam.move_one()
            elif beam.direction == DIRECTION_UP:
                beam.direction = DIRECTION_RIGHT
                beam.move_one()
            else:
                # Pipe connection no good. Die.
                break
        else:
            # Where did you go, cotton eyed joe? Die.
            break

    return energy_grid, beam.distance


def clean(grid, heatmap, replace_with='.'):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if heatmap[y][x] == 0:
                grid[y][x] = replace_with


def find_start(grid):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == 'S':
                return x, y
    return 0, 0


def find_dots(grid):
    _dots = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == '.':
                _dots.append((x, y))
    return _dots


def get(grid, x, y, fallback=None):
    if y >= len(grid) or y < 0:
        return fallback
    if x >= len(grid[y]) or x < 0:
        return fallback
    return grid[y][x]


def determine_start_type(grid, x, y) -> str:
    connect_up = get(grid, x, y - 1) in [TILE_UP_DOWN, TILE_DOWN_LEFT, TILE_DOWN_RIGHT]
    connect_down = get(grid, x, y + 1) in [TILE_UP_DOWN, TILE_UP_LEFT, TILE_UP_RIGHT]
    connect_left = get(grid, x - 1, y) in [TILE_LEFT_RIGHT, TILE_UP_RIGHT, TILE_DOWN_RIGHT]
    connect_right = get(grid, x + 1, y) in [TILE_UP_LEFT, TILE_DOWN_LEFT, TILE_LEFT_RIGHT]

    if connect_up and connect_down:
        return TILE_UP_DOWN
    elif connect_up and connect_left:
        return TILE_UP_LEFT
    elif connect_up and connect_right:
        return TILE_UP_RIGHT
    elif connect_down and connect_left:
        return TILE_DOWN_LEFT
    elif connect_down and connect_right:
        return TILE_DOWN_RIGHT
    elif connect_left and connect_right:
        return TILE_LEFT_RIGHT

    return 'S'


def determine_start_beam(start: str, x, y):
    if start in [TILE_UP_LEFT, TILE_UP_RIGHT, TILE_UP_DOWN]:
        return Beam(x, y, DIRECTION_UP)
    elif start in [TILE_DOWN_RIGHT, TILE_DOWN_LEFT]:
        return Beam(x, y, DIRECTION_DOWN)
    return Beam(x, y, DIRECTION_RIGHT)


def convert_to_cost_map(grid):
    _grid = deepcopy(grid)
    for y in range(0, len(_grid)):
        for x in range(0, len(_grid[y])):
            if _grid[y][x] == '.':
                _grid[y][x] = 2
            else:
                _grid[y][x] = -1 if _grid[y][x] in PIPES else 1

    return np.array(_grid, dtype=np.int8)


def can_path_to(dest_x, dest_y, cost_map):
    p = tpath.Dijkstra(cost_map, diagonal=0)
    mx, my = len(cost_map[0]) - 1, len(cost_map) - 1
    hx, hy = math.floor(mx / 2.0), math.floor(my / 2.0)
    # Try to path to it from all 4 corners.
    for from_x, from_y in [(0, 0), (mx, 0), (0, my), (mx, my), (0, hy), (mx, hy)]:
        if from_x == dest_x and from_y == dest_y:
            return True

        p.set_goal(dest_x, dest_y)
        route = p.get_path(from_x, from_y)
        if len(route) > 0:
            return True
    return False

from copy import deepcopy

DIRECTION_RIGHT = 0
DIRECTION_UP = 1
DIRECTION_LEFT = 2
DIRECTION_DOWN = 3

TILE_EMPTY = '.'
TILE_MIRROR_A = '|'
TILE_MIRROR_B = '\\'
TILE_MIRROR_C = '-'
TILE_MIRROR_D = '/'


class Beam:
    history: list
    x: int
    y: int
    uid: int

    direction: int

    def __init__(self, x: int, y: int, direction: int, history: list = None):
        self.history = history if history is not None else []
        self.x = x
        self.y = y
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

    def is_looping(self):
        return [self.x, self.y, self.direction] in self.history


def add_beam(others: list[Beam], to_add: Beam):
    match = False
    for b in others:
        if b.x == to_add.x and b.y == to_add.y and b.direction == to_add.direction:
            match = True
            # print('prevent addition of', to_add.uid, 'as there is a similar beam already with uid', b.uid, '.')
            break
        elif [to_add.x, to_add.y, to_add.direction] in b.history:
            match = True
            # print('prevent addition of', to_add.uid, 'as there is a similar beam that has passed there with uid', b.uid, '.')
            break

    if not match:
        others.append(to_add)


def energize(starting_beam: Beam, grid: list[list[str]]):
    starting_beam.uid = 1
    uid = 2

    energy_grid = deepcopy(grid)
    for y in range(0, len(energy_grid)):
        for x in range(0, len(energy_grid[y])):
            energy_grid[y][x] = 0

    # simulate until all the beams leave the grid
    beams = [starting_beam]
    done = False
    while not done:
        done = True
        for beam in beams:
            if (len(grid[0]) > beam.x >= 0) and (len(grid) > beam.y >= 0) and not beam.is_looping():
                done = False
                beam_tile = grid[beam.y][beam.x]
                # print(f'beam {beam.uid} is at {beam.x}, {beam.y} on {beam_tile} going {beam.dir_name()}')
                beam.log()
                energy_grid[beam.y][beam.x] = 1

                # decide action based on tile
                if beam_tile == TILE_MIRROR_A:
                    if beam.direction in [DIRECTION_UP, DIRECTION_DOWN]:
                        beam.move_one()
                    else:
                        # split. move existing beam to top going up
                        # duplicate beam to bottom going down
                        new_beam = beam.duplicate()
                        new_beam.y += 1
                        new_beam.direction = DIRECTION_DOWN
                        new_beam.uid = uid + 0
                        uid += 1
                        add_beam(beams, new_beam)
                        beam.y -= 1
                        beam.direction = DIRECTION_UP
                elif beam_tile == TILE_MIRROR_B:
                    if beam.direction == DIRECTION_LEFT:
                        beam.direction = DIRECTION_UP
                    elif beam.direction == DIRECTION_RIGHT:
                        beam.direction = DIRECTION_DOWN
                    elif beam.direction == DIRECTION_UP:
                        beam.direction = DIRECTION_LEFT
                    else:
                        beam.direction = DIRECTION_RIGHT
                    beam.move_one()
                elif beam_tile == TILE_MIRROR_C:
                    if beam.direction in [DIRECTION_LEFT, DIRECTION_RIGHT]:
                        beam.move_one()
                    else:
                        # split. move existing beam to left, going left
                        # duplicate beam to right, going right
                        new_beam = beam.duplicate()
                        new_beam.x += 1
                        new_beam.direction = DIRECTION_RIGHT
                        new_beam.uid = uid + 0
                        uid += 1
                        add_beam(beams, new_beam)
                        beam.x -= 1
                        beam.direction = DIRECTION_LEFT
                elif beam_tile == TILE_MIRROR_D:
                    if beam.direction == DIRECTION_LEFT:
                        beam.direction = DIRECTION_DOWN
                    elif beam.direction == DIRECTION_RIGHT:
                        beam.direction = DIRECTION_UP
                    elif beam.direction == DIRECTION_UP:
                        beam.direction = DIRECTION_RIGHT
                    else:
                        beam.direction = DIRECTION_LEFT
                    beam.move_one()
                else:
                    beam.move_one()

    return energy_grid
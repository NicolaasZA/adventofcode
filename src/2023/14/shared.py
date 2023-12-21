from copy import deepcopy
from hashlib import md5

ROUND_STONE = 'O'
SOLID_STONE = '#'
SPACE = '.'


def rot_90(l: list[list]):
    return [list(reversed(x)) for x in zip(*l)]


def cycle(_grid):
    # north
    _grid = apply_tilt(_grid)
    # west
    _grid = apply_tilt(rot_90(_grid))
    # south
    _grid = apply_tilt(rot_90(_grid))
    # east
    _grid = apply_tilt(rot_90(_grid))

    return rot_90(_grid)


def apply_tilt(_grid):
    _tilted = deepcopy(_grid)

    for row in range(1, len(_tilted)):
        for col in range(0, len(_tilted[row])):
            # if this location is a round stone, simulate tilt fall
            # send the stone there and remove from here
            if _tilted[row][col] == ROUND_STONE:
                _dest_row = row + 0
                while _tilted[_dest_row - 1][col] == SPACE and _dest_row > 0:
                    _dest_row -= 1

                if _dest_row != row:
                    _tilted[row][col] = SPACE
                    _tilted[_dest_row][col] = ROUND_STONE

    return _tilted


def weigh(grid):
    _weight = 0

    row_weight = len(grid)
    for row in range(0, len(grid)):
        _r = ''.join(grid[row])
        _weight += (row_weight * _r.count(ROUND_STONE))
        row_weight -= 1
    return _weight


def get_digest(grid: list[list]):
    return md5(''.join([''.join(_) for _ in grid]).encode('utf-8')).digest()

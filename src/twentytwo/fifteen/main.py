

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def taxi_dist(a: Point, b: Point) -> int:
    return abs(a.x-b.x) + abs(a.y-b.y)


def is_within_taxi_dist(s: Point, p: Point, dist: int):
    return taxi_dist(s, p) <= dist


class Sensor:
    location: Point

    dist_to_target: int

    def __init__(self, sensor: Point, beacon: Point):
        self.location = sensor
        self.beacon = beacon
        self.td = taxi_dist(sensor, beacon)

    def __repr__(self):
        return f'S({self.location.x},{self.location.y}) B({self.beacon.x},{self.beacon.y}) TD({self.td}) D({self.dist_to_target})'


def map_sensor(line: str):
    parts = line.replace('Sensor at x=', '').replace(
        ': closest beacon is at x=', ',').replace(', y=', ',').split(',')
    return Sensor(Point(int(parts[0]), int(parts[1])), Point(int(parts[2]), int(parts[3])))


def read_map(filename: str) -> list[Sensor]:
    res = []
    with open(filename, 'r') as ff:
        res = list(map(map_sensor, ff.readlines()))
    return res


def filter_out_of_range(s: Sensor):
    return s.dist_to_target <= s.td


def find_sensor_at(p: Point, sensors: list[Sensor]):
    for s in sensors:
        if s.location.x == p.x and s.location.y == p.y:
            return s
    return None


def find_beacon_at(p: Point, sensors: list[Sensor]):
    for s in sensors:
        if s.beacon.x == p.x and s.beacon.y == p.y:
            return s
    return None


def part_one(ff: str, TARGET_Y: int):
    sensors = read_map(ff)

    # Calculate distance to target y
    for s in sensors:
        s.dist_to_target = abs(s.location.y - TARGET_Y)
    sensors = list(filter(filter_out_of_range, sensors))

    # determine suitable x range
    smallest_x, largest_x = 0, 0
    for s in sensors:
        smallest_x = min(s.location.x - s.td, smallest_x)
        largest_x = max(s.location.x + s.td, largest_x)

    cannot = 0
    for x in range(smallest_x, largest_x):
        if find_sensor_at(Point(x, TARGET_Y), sensors) is not None:
            cannot += 1
        elif find_beacon_at(Point(x, TARGET_Y), sensors) is not None:
            pass
        else:
            flag = False
            for s in sensors:
                if is_within_taxi_dist(s.location, Point(x, TARGET_Y), s.td):
                    flag = True
                    break

            if flag:
                cannot += 1

    print(cannot)


if __name__ == '__main__':
    # part_one('input2.txt', 10)
    part_one('input.txt', 2000000)

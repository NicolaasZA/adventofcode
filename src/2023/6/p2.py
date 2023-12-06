def read(file_to_use) -> list[str]:
    with open(file_to_use, 'r') as _:
        return list(map(lambda x: x.replace('\n', '').replace('\r', ''), _.readlines()))


def approx_from_left(start: int, end: int, step: int, max_time: int, target_distance: int) -> int:
    for _left in range(start, end, step):
        _distance = (max_time - _left) * _left
        if _distance > target_distance:
            return _left
    return end


def approx_from_right(start: int, end: int, step: int, max_time: int, target_distance: int) -> int:
    for _right in reversed(range(start, end, step)):
        _distance = (max_time - _right) * _right
        if _distance > target_distance:
            return _right
    return end


lines = read('input.txt')

time = int(lines[0].split(':')[1].strip().replace(' ', ''))
distance = int(lines[1].split(':')[1].strip().replace(' ', ''))

print(f'time={time}')
print(f'distance={distance}')

LEFT_STEP = 100000
RIGHT_STEP = 1000000
total = 1
left, right = 1, distance

# approximate from left
left = approx_from_left(left, right, LEFT_STEP, time, distance)
print(f'left approx = {left}')
left = approx_from_left(left - LEFT_STEP, left + LEFT_STEP, 1, time, distance)
print(f'left exact = {left}')

# approximate from right
right = approx_from_right(left, right, RIGHT_STEP, time, distance)
print(f'right approx = {right}')
right = approx_from_right(right - RIGHT_STEP, right + RIGHT_STEP, 1, time, distance)
print(f'right exact = {right}')

# calculate the range
total *= (right - left + 1)
print(total)

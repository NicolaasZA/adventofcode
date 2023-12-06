def read(file_to_use) -> list[str]:
    with open(file_to_use, 'r') as _:
        return list(map(lambda x: x.replace('\n', '').replace('\r', ''), _.readlines()))


lines = read('input.txt')

times = [int(_) for _ in lines[0].split(':')[1].strip().split(' ') if _ != '']
distances = [int(_) for _ in lines[1].split(':')[1].strip().split(' ') if _ != '']

races = [(times[_], distances[_]) for _ in range(0, len(times))]

print(f'times={times}')
print(f'distances={distances}')
print(f'races={races}')

total = 1
for time, distance in races:
    left, right = 1, distance

    # look from left
    for hold_time in range(left, right):
        traveled_distance = (time - hold_time) * hold_time
        if traveled_distance > distance:
            left = hold_time
            break

    # look from right
    for hold_time in reversed(range(left, right)):
        traveled_distance = (time - hold_time) * hold_time
        if traveled_distance > distance:
            right = hold_time
            break

    # calculate the range
    total *= (right - left + 1)
    print(left, right, (right - left + 1))
print(total)

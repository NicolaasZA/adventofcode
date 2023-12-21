from shared import convert, expand, dist, fast_dist
import time


raw = [[c for c in line.strip()] for line in open('input.txt').readlines()]
chart, _ = convert(raw)

stars = expand(chart, factor=1_000_000)

time_start = time.perf_counter()

total = 0
for start in range(0, len(stars)):
    for end in range(start + 1, len(stars)):
        _a = stars[start]
        _b = stars[end]
        d = fast_dist(_a, _b)
        # d = dist(_a.x, _a.y, _b.x, _b.y)
        total += d

print(f'Part 2: {total}')  # 363293506944

time_duration = round((time.perf_counter() - time_start) * 1000.0, 1)
print(f'took {time_duration} milliseconds')

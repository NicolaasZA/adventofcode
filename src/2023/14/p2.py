from shared import cycle, weigh, get_digest

grid = [[_ for _ in line.strip()] for line in open('input.txt').readlines()]

duplicate_digests = []
digests = []
digest_weights = []
i = 1
target = 1_000_000_000
start: int = -1
while i <= target:
    grid = cycle(grid)
    d = str(get_digest(grid))

    if d in digests:
        if start == -1:
            start = i
        if d in duplicate_digests:
            break
        else:
            duplicate_digests.append(d)
            digest_weights.append(weigh(grid))
    digests.append(d)
    i += 1

loop_location = (target - start) % len(duplicate_digests)

print(digest_weights[loop_location])


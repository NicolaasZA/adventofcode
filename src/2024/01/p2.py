def read_pairs(filename: str):
    left, right = [], []
    with open(filename, 'r') as file:
        content = file.readlines()
        for line in content:
            sides = line.split(" ")
            left.append(int(sides[0]))
            right.append(int(sides[-1]))
    return sorted(left), sorted(right)


def count_of(target: int, data: list[int]) -> int:
    return


l, r = read_pairs("data.txt")

score = 0
for idx in range(len(l)):
    score += l[idx] * r.count(l[idx])

print(score)
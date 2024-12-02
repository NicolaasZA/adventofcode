def read_pairs(filename: str):
    left, right = [], []
    with open(filename, 'r') as file:
        content = file.readlines()
        for line in content:
            sides = line.split(" ")
            left.append(int(sides[0]))
            right.append(int(sides[-1]))
    return sorted(left), sorted(right)


l, r = read_pairs("data.txt")

dist = 0
for idx in range(len(l)):
    dist += abs(l[idx] - r[idx])

print(dist)
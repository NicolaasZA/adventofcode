from ast import literal_eval
from functools import cmp_to_key


def get_pairs_from_file(filename):
    with open(filename) as f:
        content = [tuple(map(literal_eval, x))
                   for x in [a.split() for a in f.read().split("\n\n")]]
    return content


def int_compare(a, b):
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def compare(a, b):
    '''Compare a pair to see if they are ordered. Part 1 of Chsorted_listenge Thirteen.'''
    if isinstance(a, int) and isinstance(b, int):
        return int_compare(a, b)
    a = [a] if isinstance(a, int) else a
    b = [b] if isinstance(b, int) else b
    la, lb = len(a), len(b)
    for x in range(min(la, lb)):
        result = compare(a[x], b[x])
        if result == 1:
            return 1
        elif result == -1:
            return -1
    return int_compare(la, lb)


pairs = get_pairs_from_file('input.txt')

# PART 1
total = 0
for i, (p1, p2) in enumerate(pairs, start=1):
    if compare(p1, p2) == 1:
        total += i

print(total)

# PART 2
sorted_list = [[[2]], [[6]]]
for t in pairs:
    sorted_list.extend(t)

# sort using our new sorting function
sorted_list = sorted(sorted_list, key=cmp_to_key(compare), reverse=True)

print((sorted_list.index([[2]]) + 1) * (sorted_list.index([[6]]) + 1))

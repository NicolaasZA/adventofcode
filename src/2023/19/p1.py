import sys

from shared import Workflow, Rating

lines = [line.strip() for line in open('input.txt').readlines()]

workflows = [Workflow(_) for _ in lines[:lines.index('')]]
ratings = [(Rating.from_string(_), 'in') for _ in lines[lines.index('') + 1:]]


def find_flow(name: str):
    for f in workflows:
        if f.name == name:
            return f
    return None


def is_done():
    for r, f in ratings:
        if f not in ['A', 'R']:
            return False
    return True


# for flow in workflows:
#     print(flow.name, flow.rules)

starting_flow: Workflow = find_flow('in')
if starting_flow is None:
    sys.exit(0)

while not is_done():
    for idx in range(0, len(ratings)):
        rating, current_flow = ratings[idx]
        if current_flow in ['A', 'R']:
            continue

        flow = find_flow(current_flow)
        result = flow.apply(rating)
        # print(rating, '==>', result)
        ratings[idx] = rating, result

total = 0
for r, f in ratings:
    if f == 'A':
        total += (r['x'] + r['m'] + r['a'] + r['s'])

print(total)

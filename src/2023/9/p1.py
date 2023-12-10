from shared import Reading

readings = [Reading(_.strip()) for _ in open('input.txt').readlines()]

total = []
for r in readings:
    r.build_layers()
    _next = r.predict_next()
    total.append(_next)

print(f'Part 1: {sum(total)}')  # 1853145119
# part 2: 923

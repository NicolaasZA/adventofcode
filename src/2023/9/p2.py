from shared import Reading

readings = [Reading(_.strip()) for _ in open('input.txt').readlines()]

total = []
for r in readings:
    r.build_layers()
    _next = r.predict_previous()
    total.append(_next)

print(f'Part 2: {sum(total)}')  # 923

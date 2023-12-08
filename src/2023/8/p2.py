import math

from shared import Mapping

L = [line.strip() for line in open('input.txt').readlines() if line.strip() != '']
steps = L[0]
mappings = {}

for line in L[1:]:
    m: Mapping = Mapping(line)
    mappings[m.name] = m

steppers = [mappings[key].name for key in mappings if mappings[key].end == 'A']

counters = []
for stepper in steppers:
    step_count, step_index, step_at = 0, 0, stepper
    while step_at[-1] != 'Z':
        m = mappings[step_at]
        step_at = m.step(steps[step_index])
        step_count += 1
        step_index = (step_index + 1) % len(steps)
    counters.append(step_count)


print('Part 2:', math.lcm(*counters))

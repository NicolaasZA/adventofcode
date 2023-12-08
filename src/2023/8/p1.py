from shared import Mapping

L = [line.strip() for line in open('input.txt').readlines() if line.strip() != '']
steps = L[0]
mappings = {}

for line in L[1:]:
    m: Mapping = Mapping(line)
    mappings[m.name] = m

out = open('result.txt', mode='x')
step_count, step_index, step_at = 0, 0, 'AAA'
while step_count < 500000:
# while step_at != 'ZZZ':
    out.write(step_at + '\n')
    m = mappings[step_at]
    step_at = m.step(steps[step_index])
    step_count += 1
    step_index = (step_index + 1) % len(steps)

out.write(step_at + '\n')

print('Part 1:', step_count)
out.flush()
out.close()
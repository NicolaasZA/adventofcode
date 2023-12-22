import sys

grid = [[int(x) for x in row.strip()] for row in open('input.txt').readlines()]

max_x = len(grid[0])
max_y = len(grid)

states_for_cost = {}
cost_for_state = {}


def move_add_state(cost: int, x: int, y: int, delta_x: int, delta_y: int, dist: int):
    x += delta_x
    y += delta_y

    if x < 0 or y < 0:
        return
    if x >= max_x or y >= max_y:
        return

    new_cost = cost + grid[y][x]
    # Here we need a distance of 4 or greater to stop
    if x == (max_x - 1) and y == (max_y - 1) and dist >= 4:
        # Show answer and stop
        print(new_cost)
        sys.exit(0)

    # Create the state
    state = (x, y, delta_x, delta_y, dist)
    if state not in cost_for_state:
        states_for_cost.setdefault(new_cost, []).append(state)
        cost_for_state[state] = new_cost


# add our starting states, then run
move_add_state(0, 0, 0, 1, 0, 1)
move_add_state(0, 0, 0, 0, 1, 1)

while True:
    current_cost = min(states_for_cost.keys())

    # Calculate next
    next_states = states_for_cost.pop(current_cost)
    for (x, y, dx, dy, distance) in next_states:

        if distance >= 4:
            # We can turn
            move_add_state(current_cost, x, y, dy, -dx, 1)
            move_add_state(current_cost, x, y, -dy, dx, 1)

        if distance < 10:
            # We can go straight
            move_add_state(current_cost, x, y, dx, dy, distance + 1)

from collections import deque

def solve_monkey_banana():
    initial_state = ('door', 'window', False, False)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()
        monkey_pos, box_pos, on_box, has_banana = state

        if has_banana:
            return actions

        if state in visited:
            continue
        visited.add(state)

        locations = ['door', 'window', 'middle']

        if not on_box:
            for loc in locations:
                if loc != monkey_pos:
                    next_state = (loc, box_pos, False, False)
                    queue.append((next_state, actions + [f"Walk from {monkey_pos} to {loc}"]))

            if monkey_pos == box_pos:
                for loc in locations:
                    if loc != monkey_pos:
                        next_state = (loc, loc, False, False)
                        queue.append((next_state, actions + [f"Push box from {monkey_pos} to {loc}"]))

                next_state = (monkey_pos, box_pos, True, False)
                queue.append((next_state, actions + ["Climb onto the box"]))

        if on_box and monkey_pos == 'middle':
            next_state = (monkey_pos, box_pos, True, True)
            queue.append((next_state, actions + ["Grasp the banana"]))

    return []

plan = solve_monkey_banana()
print("Optimal Action Plan for Monkey and Banana Problem:")
for idx, step in enumerate(plan, 1):
    print(f"{idx}. {step}")

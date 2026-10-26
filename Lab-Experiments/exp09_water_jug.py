from collections import deque

def water_jug_solver(cap1, cap2, target):
    visited = set()
    queue = deque([[(0, 0)]])

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        if x == target or y == target:
            return path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        next_states = [
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            (x + min(y, cap1 - x), y - min(y, cap1 - x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(path + [state])

    return None

steps = water_jug_solver(4, 3, 2)
print("Water Jug Solution Steps (Jug1, Jug2):")
for step in steps:
    print(step)

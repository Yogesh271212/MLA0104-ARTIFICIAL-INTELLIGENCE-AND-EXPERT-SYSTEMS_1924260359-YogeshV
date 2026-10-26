import heapq

def a_star(graph, heuristics, start, goal):
    open_list = [(heuristics[start], 0, start, [start])]
    visited = {}

    while open_list:
        f_cost, g_cost, current, path = heapq.heappop(open_list)

        if current == goal:
            return g_cost, path

        if current in visited and visited[current] <= g_cost:
            continue
        visited[current] = g_cost

        for neighbor, weight in graph.get(current, []):
            new_g = g_cost + weight
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return float('inf'), []

graph = {
    'Start': [('NodeA', 1), ('NodeB', 4)],
    'NodeA': [('NodeB', 2), ('NodeC', 5), ('Goal', 12)],
    'NodeB': [('NodeC', 2)],
    'NodeC': [('Goal', 3)],
    'Goal': []
}

heuristics = {
    'Start': 7,
    'NodeA': 6,
    'NodeB': 2,
    'NodeC': 1,
    'Goal': 0
}

cost, path = a_star(graph, heuristics, 'Start', 'Goal')
print("Optimal Path:", " -> ".join(path))
print("Total Optimal Cost:", cost)

import heapq

def greedy_bfs(graph, heuristics, start, goal):
    pq = [(heuristics[start], start)]
    visited = set()
    path = []

    while pq:
        _, current = heapq.heappop(pq)
        if current in visited:
            continue

        path.append(current)
        visited.add(current)

        if current == goal:
            return path

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor))

    return None

graph = {
    'Entrance': ['Rack1', 'Rack2'],
    'Rack1': ['Rack3', 'Rack4'],
    'Rack2': ['Rack5'],
    'Rack3': [],
    'Rack4': ['TargetRack'],
    'Rack5': ['TargetRack'],
    'TargetRack': []
}

heuristics = {
    'Entrance': 12,
    'Rack1': 7,
    'Rack2': 5,
    'Rack3': 6,
    'Rack4': 2,
    'Rack5': 3,
    'TargetRack': 0
}

route = greedy_bfs(graph, heuristics, 'Entrance', 'TargetRack')
print("Greedy Best First Search Route:", " -> ".join(route))

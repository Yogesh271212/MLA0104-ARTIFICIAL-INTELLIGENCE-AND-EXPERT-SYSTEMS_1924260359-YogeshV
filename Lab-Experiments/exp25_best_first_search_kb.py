import heapq

edges = {
    'A': [('B', 5), ('C', 3)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 0)],
    'F': [('G', 0)],
    'G': []
}

def heuristic_search(start, goal):
    pq = [(10, start, [start])]
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        visited.add(node)
        for neighbor, h_val in edges.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (h_val, neighbor, path + [neighbor]))
    return []

best_route = heuristic_search('A', 'G')
print("Best Route Located:", " -> ".join(best_route))

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = []
    if path is None:
        path = []

    visited.append(start)
    path = path + [start]

    if start == goal:
        return visited, path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            _, result_path = dfs(graph, neighbor, goal, visited, path)
            if result_path:
                return visited, result_path

    return visited, None

graph = {
    'Cave1': ['Cave2', 'Cave3'],
    'Cave2': ['Cave4', 'Cave5'],
    'Cave3': ['Cave6'],
    'Cave4': [],
    'Cave5': ['Cave6'],
    'Cave6': []
}

visited_nodes, path = dfs(graph, 'Cave1', 'Cave6')
print("DFS Traversal:", " -> ".join(visited_nodes))
print("Path Found:", " -> ".join(path))

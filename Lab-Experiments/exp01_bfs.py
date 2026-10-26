from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    visited.add(start)
    traversal = []

    while queue:
        path = queue.popleft()
        node = path[-1]
        traversal.append(node)

        if node == goal:
            return traversal, path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return traversal, None

graph = {
    'RoomA': ['RoomB', 'RoomC'],
    'RoomB': ['RoomD', 'RoomE'],
    'RoomC': ['RoomF'],
    'RoomD': [],
    'RoomE': ['RoomF'],
    'RoomF': []
}

traversal, shortest_path = bfs(graph, 'RoomA', 'RoomF')
print("Level-wise Traversal:", " -> ".join(traversal))
print("Shortest Path:", " -> ".join(shortest_path))

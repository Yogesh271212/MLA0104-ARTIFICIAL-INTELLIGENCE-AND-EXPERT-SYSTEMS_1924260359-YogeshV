import heapq

def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + weight, neighbor, path + [neighbor]))

    return float('inf'), []

graph = {
    'Warehouse': [('HubA', 4), ('HubB', 2)],
    'HubA': [('HubC', 5), ('Destination', 10)],
    'HubB': [('HubA', 1), ('HubC', 8)],
    'HubC': [('Destination', 2)],
    'Destination': []
}

min_cost, best_path = ucs(graph, 'Warehouse', 'Destination')
print("Least-Cost Path:", " -> ".join(best_path))
print("Minimum Transportation Cost:", min_cost)

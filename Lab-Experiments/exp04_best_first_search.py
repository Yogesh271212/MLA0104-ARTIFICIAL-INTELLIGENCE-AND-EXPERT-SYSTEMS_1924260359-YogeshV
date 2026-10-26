import heapq

def best_first_search(graph, heuristics, start, goal):
    open_list = [(heuristics[start], start, [start])]
    visited = set()

    while open_list:
        h_val, current, path = heapq.heappop(open_list)

        if current == goal:
            return path

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None

graph = {
    'CityA': ['CityB', 'CityC'],
    'CityB': ['CityD', 'CityE'],
    'CityC': ['CityF'],
    'CityD': [],
    'CityE': ['CityG'],
    'CityF': ['CityG'],
    'CityG': []
}

heuristics = {
    'CityA': 10,
    'CityB': 8,
    'CityC': 5,
    'CityD': 7,
    'CityE': 3,
    'CityF': 2,
    'CityG': 0
}

path = best_first_search(graph, heuristics, 'CityA', 'CityG')
print("Best First Search Path:", " -> ".join(path))

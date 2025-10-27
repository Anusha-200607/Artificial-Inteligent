import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue: (cost, path)
    queue = [(0, [start])]
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(queue, (cost + edge_cost, new_path))

    return float("inf"), []


# 👇 Input inside program
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

start, goal = 'A', 'G'
cost, path = uniform_cost_search(graph, start, goal)

print("Uniform Cost Search (UCS)")
print("--------------------------")
print(f"Graph: {graph}")
print(f"Start: {start}, Goal: {goal}")
print(f"Least Cost Path: {' -> '.join(path)} with total cost = {cost}")

import heapq

def a_star_search(graph, start, goal, heuristic):
    queue = [(heuristic[start], 0, [start])]
    visited = set()

    while queue:
        est_total, cost_so_far, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return cost_so_far, path

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph.get(node, []):
                new_cost = cost_so_far + edge_cost
                est_cost = new_cost + heuristic[neighbor]
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(queue, (est_cost, new_cost, new_path))

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

heuristic = {
    'A': 7, 'B': 6, 'C': 2, 'D': 5, 'E': 1, 'F': 4, 'G': 0
}

start, goal = 'A', 'G'
cost, path = a_star_search(graph, start, goal, heuristic)

print("\nA* Search Algorithm")
print("-------------------")
print(f"Graph: {graph}")
print(f"Heuristic: {heuristic}")
print(f"Start: {start}, Goal: {goal}")
print(f"Optimal Path: {' -> '.join(path)} with total cost = {cost}")

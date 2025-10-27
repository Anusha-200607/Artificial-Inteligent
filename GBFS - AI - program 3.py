import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    # Priority queue to select node with the lowest heuristic value
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], [start]))
    visited = set()

    while priority_queue:
        # Pop the node with the smallest heuristic value
        _, path = heapq.heappop(priority_queue)
        node = path[-1]

        if node not in visited:
            visited.add(node)

            # If goal is reached
            if node == goal:
                return path

            # Explore neighbors
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    heapq.heappush(priority_queue, (heuristic[neighbor], new_path))

    return None


# 👇 Input given inside the program
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['H'],
    'H': []
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 4,
    'G': 3,
    'H': 0   # Goal node has 0 distance
}

start_node = 'A'
goal_node = 'H'

# Run GBFS
result = greedy_best_first_search(graph, start_node, goal_node, heuristic)

# Display Output
print("Greedy Best-First Search (GBFS) Algorithm in AI")
print("------------------------------------------------")
print("Graph:", graph)
print("Heuristic Values:", heuristic)
print(f"Start Node: {start_node}")
print(f"Goal Node: {goal_node}")

if result:
    print("Path Found:", " -> ".join(result))
else:
    print("No path found.")

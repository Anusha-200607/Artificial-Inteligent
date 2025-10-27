from collections import deque

def bfs(graph, start_node, goal_node):
    visited = set()
    queue = deque([[start_node]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            if node == goal_node:
                return path  # Return the path from start to goal

            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  # If no path found


# 👇 Input is given inside the program itself
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

start_node = 'A'   # Starting point
goal_node = 'H'    # Goal node

# Run BFS
result = bfs(graph, start_node, goal_node)

# Display Output
print("Breadth-First Search (BFS) Algorithm in AI")
print("-------------------------------------------")
print("Graph:", graph)
print(f"Start Node: {start_node}")
print(f"Goal Node: {goal_node}")

if result:
    print("Path Found:", " -> ".join(result))
else:
    print("No path found.")

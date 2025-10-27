def dfs(graph, start_node, goal_node):
    # Stack to keep track of paths
    stack = [[start_node]]
    visited = set()

    while stack:
        # Get the last path from the stack (LIFO)
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            # If goal is found, return path
            if node == goal_node:
                return path

            # Explore neighbors (reversed for correct order)
            for neighbor in reversed(graph.get(node, [])):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return None


# 👇 Input given inside the program
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

start_node = 'A'   # Starting node
goal_node = 'H'    # Goal node

# Run DFS
result = dfs(graph, start_node, goal_node)

# Display Output
print("Depth-First Search (DFS) Algorithm in AI")
print("----------------------------------------")
print("Graph:", graph)
print(f"Start Node: {start_node}")
print(f"Goal Node: {goal_node}")

if result:
    print("Path Found:", " -> ".join(result))
else:
    print("No path found.")

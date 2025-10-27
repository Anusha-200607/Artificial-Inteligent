from collections import deque

def water_jug_problem(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])  # (x, y)

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        print(f"({x}, {y})")  # show each step

        if x == target or y == target:
            print("\nGoal reached!")
            return True

        # Possible operations
        queue.extend([
            (jug1, y),  # Fill jug1
            (x, jug2),  # Fill jug2
            (0, y),     # Empty jug1
            (x, 0),     # Empty jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour jug1 -> jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour jug2 -> jug1
        ])
    return False


# 👇 Input inside program
jug1, jug2, target = 4, 3, 2
print("\nWater Jug Problem")
print("-----------------")
print(f"Jug1 = {jug1}L, Jug2 = {jug2}L, Target = {target}L\n")
water_jug_problem(jug1, jug2, target)

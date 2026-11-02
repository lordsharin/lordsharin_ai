
# DFS for Water Jug Problem

# Jug capacities
A = 4
B = 3

# Goal: Get 2 litres in Jug A
goal = 2

# Store visited states
visited = []

# DFS Function
def dfs(x, y):

    # Check if state is already visited
    if (x, y) in visited:
        return False

    visited.append((x, y))

    print("Jug A:", x, "Jug B:", y)

    # Check goal condition
    if x == goal:
        return True

    # Generate possible operations
    next_states = [
        (A, y),                         # Fill Jug A
        (x, B),                         # Fill Jug B
        (0, y),                         # Empty Jug A
        (x, 0),                         # Empty Jug B
        (x - min(x, B - y), y + min(x, B - y)),  # Pour A to B
        (x + min(y, A - x), y - min(y, A - x))   # Pour B to A
    ]

    # Explore next states
    for state in next_states:

        if dfs(state[0], state[1]):
            return True

    return False


# Main Program
print("Water Jug Problem using DFS")

if dfs(0, 0):
    print("\nGoal Reached!")
else:
    print("\nSolution Not Found!")

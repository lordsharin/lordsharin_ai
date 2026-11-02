
# A* Search Algorithm for 8 Puzzle Problem

# Initial State
start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

# Goal State
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

# Calculate Manhattan Distance (Heuristic)
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])

            x1, y1 = i // 3, i % 3
            x2, y2 = goal_index // 3, goal_index % 3

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Find possible next states
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_index = new_row * 3 + new_col

            new_state = state.copy()

            new_state[zero], new_state[new_index] = (
                new_state[new_index], new_state[zero]
            )

            neighbors.append(new_state)

    return neighbors


# A* Search Algorithm
def astar(start):

    open_list = [(start, 0)]
    visited = set()

    while open_list:

        # Select state with lowest f(n)
        open_list.sort(key=lambda x: x[1])

        current, cost = open_list.pop(0)

        if tuple(current) in visited:
            continue

        visited.add(tuple(current))

        print("\nCurrent State:")
        for i in range(0, 9, 3):
            print(current[i:i+3])

        # Check goal
        if current == goal:
            print("\nGoal State Reached!")
            return

        # Generate next states
        for neighbor in get_neighbors(current):

            if tuple(neighbor) not in visited:

                g = cost + 1
                h = heuristic(neighbor)

                f = g + h

                open_list.append((neighbor, f))

    print("Solution Not Found!")


# Run Program
print("Initial State:")
for i in range(0, 9, 3):
    print(start[i:i+3])

astar(start)


# BFS for Robot Path Planning

from collections import deque

# Grid environment
grid = [
    ['S', '0', '0', 'X'],
    ['X', 'X', '0', 'X'],
    ['0', '0', '0', '0'],
    ['0', 'X', 'X', 'G']
]

# Starting and goal positions
start = (0, 0)
goal = (3, 3)

# Possible movements: Up, Down, Left, Right
moves = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

# BFS Algorithm
def bfs(start, goal):

    queue = deque([(start, [start])])
    visited = [start]

    while queue:

        position, path = queue.popleft()

        # Check goal
        if position == goal:
            return path

        x, y = position

        # Check all possible movements
        for move in moves:

            new_x = x + move[0]
            new_y = y + move[1]

            # Check grid boundaries
            if (0 <= new_x < 4 and 0 <= new_y < 4):

                # Check obstacle and visited position
                if (grid[new_x][new_y] != 'X' and
                    (new_x, new_y) not in visited):

                    new_position = (new_x, new_y)

                    visited.append(new_position)

                    new_path = path + [new_position]

                    queue.append((new_position, new_path))

    return None


# Main Program
print("Initial Grid:")

for row in grid:
    print(row)

path = bfs(start, goal)

if path:
    print("\nPath Found:")
    print(path)

    print("\nNumber of Steps:", len(path) - 1)

else:
    print("\nNo Path Found!")


# Model-Based Intelligent Agent with Obstacles

# Grid Environment
grid = [
    ['S', '0', 'X', '0'],
    ['0', '0', 'X', '0'],
    ['X', '0', '0', '0'],
    ['0', '0', '0', 'G']
]

# Starting position
position = [0, 0]

# Internal state representation
visited = []

print("Initial Grid:")
for row in grid:
    print(row)

# Movement directions
moves = [
    [0, 1],   # Right
    [1, 0],   # Down
    [0, -1],  # Left
    [-1, 0]   # Up
]

# Model-Based Agent
while True:

    x = position[0]
    y = position[1]

    # Check goal
    if grid[x][y] == 'G':
        print("\nGoal Reached!")
        break

    visited.append([x, y])

    moved = False

    # Check possible movements
    for move in moves:

        new_x = x + move[0]
        new_y = y + move[1]

        # Check grid boundaries
        if (new_x >= 0 and new_x < 4 and
            new_y >= 0 and new_y < 4):

            # Check obstacles and visited positions
            if (grid[new_x][new_y] != 'X' and
                [new_x, new_y] not in visited):

                position = [new_x, new_y]
                print("Agent moved to:", position)

                moved = True
                break

    # Stop if no movement is possible
    if moved == False:
        print("\nNo path found!")
        break

print("\nVisited Positions:")
print(visited)


# Local Beam Search for Traveling Salesman Problem

import random

# Distance between cities
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [0, 1, 2, 3]

# Calculate total distance of a path
def calculate_distance(path):
    total = 0

    for i in range(len(path) - 1):
        total += distance[path[i]][path[i + 1]]

    total += distance[path[-1]][path[0]]

    return total


# Generate neighboring paths
def get_neighbors(path):
    neighbors = []

    for i in range(1, len(path)):
        for j in range(i + 1, len(path)):

            new_path = path.copy()

            new_path[i], new_path[j] = (
                new_path[j], new_path[i]
            )

            neighbors.append(new_path)

    return neighbors


# Local Beam Search
def local_beam_search(k):

    # Initial paths
    beam = [cities.copy()]

    for _ in range(k - 1):
        new_path = cities.copy()
        random.shuffle(new_path[1:])
        beam.append(new_path)

    best_path = None
    best_cost = float('inf')

    # Search process
    for step in range(10):

        all_neighbors = []

        for path in beam:
            neighbors = get_neighbors(path)
            all_neighbors.extend(neighbors)

        # Sort paths by distance
        all_neighbors.sort(key=calculate_distance)

        # Select best k paths
        beam = all_neighbors[:k]

        # Find best path
        if calculate_distance(beam[0]) < best_cost:
            best_path = beam[0]
            best_cost = calculate_distance(beam[0])

    return best_path, best_cost


# Main Program
k = 2

path, cost = local_beam_search(k)

print("Best Path:", path)
print("Minimum Distance:", cost)

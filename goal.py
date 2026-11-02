
# Goal Stack Planning - Blocks World Problem

# Initial State
current_state = [
    "A on Table",
    "B on Table",
    "C on Table",
    "Clear A",
    "Clear B",
    "Clear C"
]

# Goal State
goal_state = [
    "A on B",
    "B on C"
]


# Function to perform actions
def perform(action):

    if action == "Move B to C":

        current_state.remove("B on Table")
        current_state.remove("Clear C")

        current_state.append("B on C")

    elif action == "Move A to B":

        current_state.remove("A on Table")
        current_state.remove("Clear B")

        current_state.append("A on B")

    print("\nAction:", action)
    print("Current State:", current_state)


# Main Program
print("Initial State:", current_state)

# Achieve first goal
if "B on C" not in current_state:
    perform("Move B to C")

# Achieve second goal
if "A on B" not in current_state:
    perform("Move A to B")


# Check Final Goal
print("\nFinal State:", current_state)

if ("A on B" in current_state and
    "B on C" in current_state):

    print("\nGoal Achieved Successfully!")

else:
    print("\nGoal Not Achieved!")

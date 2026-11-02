
# Simple Reflex Agent - Vacuum Cleaner World

# Initial environment
A = "Dirty"
B = "Dirty"

# Current position of vacuum cleaner
location = "A"

print("Initial Environment:")
print("Room A:", A)
print("Room B:", B)
print("Vacuum Cleaner is at:", location)

# Simple Reflex Agent
while A == "Dirty" or B == "Dirty":

    if location == "A":

        if A == "Dirty":
            print("\nRoom A is Dirty. Action: SUCK")
            A = "Clean"

        else:
            print("\nRoom A is Clean. Action: MOVE RIGHT")
            location = "B"

    elif location == "B":

        if B == "Dirty":
            print("\nRoom B is Dirty. Action: SUCK")
            B = "Clean"

        else:
            print("\nRoom B is Clean. Action: MOVE LEFT")
            location = "A"

print("\nFinal Environment:")
print("Room A:", A)
print("Room B:", B)
print("All rooms are Clean!")

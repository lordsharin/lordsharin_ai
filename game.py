
# Minimax Algorithm - Tic Tac Toe Game

# Create the game board
board = ["-" for i in range(9)]

# Display the board
def display_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()


# Check winner
def check_winner():

    win_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for pos in win_positions:
        a, b, c = pos

        if board[a] == board[b] == board[c] == "X":
            return "X"

        if board[a] == board[b] == board[c] == "O":
            return "O"

    return None


# Check if board is full
def is_full():
    return "-" not in board


# Minimax Algorithm
def minimax(is_maximizing):

    winner = check_winner()

    if winner == "X":
        return 1

    if winner == "O":
        return -1

    if is_full():
        return 0

    if is_maximizing:

        best_score = -100

        for i in range(9):

            if board[i] == "-":

                board[i] = "X"

                score = minimax(False)

                board[i] = "-"

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = 100

        for i in range(9):

            if board[i] == "-":

                board[i] = "O"

                score = minimax(True)

                board[i] = "-"

                best_score = min(score, best_score)

        return best_score


# Computer's move
def computer_move():

    best_score = -100
    best_move = -1

    for i in range(9):

        if board[i] == "-":

            board[i] = "X"

            score = minimax(False)

            board[i] = "-"

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "X"

    print("Computer played!")


# Human's move
def human_move():

    while True:

        move = int(input("Enter position (1-9): ")) - 1

        if 0 <= move < 9 and board[move] == "-":

            board[move] = "O"
            break

        else:
            print("Invalid move! Try again.")


# Main Program
print("TIC TAC TOE - MINIMAX ALGORITHM")

print("Positions:")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")

while True:

    display_board()

    human_move()

    if check_winner() == "O":
        display_board()
        print("Human Wins!")
        break

    if is_full():
        display_board()
        print("Game Draw!")
        break

    computer_move()

    if check_winner() == "X":
        display_board()
        print("Computer Wins!")
        break

    if is_full():
        display_board()
        print("Game Draw!")
        break

board = [" "] * 9

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

def full():
    return " " not in board

def ai_move():

    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check("O"):
                return
            board[i] = " "

    # Block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check("X"):
                board[i] = "O"
                return
            board[i] = " "

    # Otherwise take first empty place
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return

print("Tic Tac Toe")
print("You = X")
print("Computer = O")

while True:

    show_board()

    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8:
        print("Invalid position")
        continue

    if board[move] != " ":
        print("Already filled")
        continue

    board[move] = "X"

    if check("X"):
        show_board()
        print("You Win!")
        break

    if full():
        show_board()
        print("Match Draw")
        break

    ai_move()

    if check("O"):
        show_board()
        print("Computer Wins!")
        break

    if full():
        show_board()
        print("Match Draw")
        break
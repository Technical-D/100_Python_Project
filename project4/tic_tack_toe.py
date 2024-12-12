def display_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != (len(row) - 1):
                row_str += " | "
        
        print(row_str)
        if i != (len(board) -1):
            print("-----------")

def get_move(turn, board):

    while True:
        row = int(input("Row: "))
        col = int(input("Col: "))

        if row < 1 or row > len(board):
            print("Invalid row, try again!")
        elif col < 1 or row > len(board[row - 1]):
            print("Invalid column, tey again!")
        elif board[row -1][col - 1] != " ":
            print("Already taken, try again!")
        else:
            break

    board[row - 1][col - 1] = turn

def check_win(board, turn):
    lines = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
    ]
    for line in lines:
        win = True
        for pos in line:
            row, col = pos
            if board[row][col] != turn:
                win = False
                break
        if win:
            return True
    return False

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turn = "X"
print("Tic-Tac-Toe")
display_board(board)
turn_num = 0
while turn_num < 9:
    print()
    print("It is the", turn, "players turn. Please select you move.")
    get_move(turn, board)
    display_board(board)
    if check_win(board, turn):
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    
    turn_num += 1

if turn_num == 9:
    print("Game Tied!")
else:
    print(turn,"player won the game!")
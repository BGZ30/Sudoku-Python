board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(board):
    for r in range(9):
        if r%3 == 0 and r != 0:
            print("-------------------------")
        
        for c in range(9):
            if c%3 == 0 and c != 0:
                print(" | ", end="")

            # if c==8, print the number and move to a new line. Else print on the same line.
            if c == 8:
                print(str(board[r][c]))
            else:
                print(str(board[r][c]) + " ", end="")
                
print_board(board)
""" Complete code to solve a sudoku board"""

def solve_sudoku(board):
    cell = find_cell(board)
    if not cell:
        # there is no empty cell, so the board is fully solved
        return True
        
    else:
        row, col = cell
            
    # check all numbers (1-9) to find which fits in that cell
    # use callbacking to find the best fits
    for n in range(1, 10):
        if is_valid(board, n, (row, col)):
            board[row][col] = n
            
            # recursion
            # solve for the next emptu cell
            if solve_sudoku(board):
                return True # it's solved
                
            # callbacking
            board[row][col] = 0
            
    return False    # can't find a solution, so callbacking
    

def is_valid(board, num, pos):
    """
        args:
            board: 9x9 array, the sudoku board.
            num: (int), the inserted number in a free cell.
            pos: tuple, position of an empty cell in the sudoku board.
            
        returns True if the inserted number (num) doesn't break the board.
    """
    # check row
    for c in range(9):
        # iterate over each cell in the row pos[0], and exclude the "pos" itself
        if board[pos[0]][c] == num and pos[1] != c:
            return False
            
    # check column
    for r in range(9):
        # iterate over each cell in the col pos[1], and exclude the "pos" itself
        if board[r][pos[1]] == num and pos[0] != r:
            return False
    
    # check subbox
    ''' index of subbox is (box_x, box_y) '''
    box_x = pos[1]//3
    box_y = pos[0]//3
    
    for bx in range(box_y*3, box_y*3+3):
        for by in range(box_x*3, box_x*3+3):
        # iterate over each cell in the subbox, and exclude the "pos" itself
            if board[bx][by] == num and (bx, by) != pos:
                return False
                
    return True
    
    
""" find an empty cell in the sudoku board"""
def find_cell(board):
    for r in range(9):
        for c in range(9):            
            if board[r][c] == 0:
                return (r, c)  # the cell index
    
    return None # no empty cells found
  
  
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
                
print("Original is :")
print_board(board)
solve_sudoku(board)
print("**************************")
print("Solved is:")
print_board(board)
            
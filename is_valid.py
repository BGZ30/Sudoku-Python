
""" check if the inserted number is valid and not break the rules of sudoku"""
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
                      

"""
    cell (0, 5) is Invalid; row error
    cell (4, 4) is Invalid; col error
    cell (6, 7) is Invalid; subbox error
    cell (1, 0) is valid
"""
board = [
    [7, 8, 0, 4, 0, 2, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 7, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    
    [0, 7, 0, 3, 0, 0, 0, 4, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Test
if is_valid(board, 2, (0,5)):
    print("num 2 in cell (0,5) is valid")
else:
    print("num 2 in cell (0,5) is Invalid")

if is_valid(board, 7, (4, 4)):
    print("num 7 in cell (4, 4) is valid")
else:
    print("num 7 in cell (4, 4) is Invalid")

if is_valid(board, 4, (6, 7)):
    print("num 4 in cell (6, 7) is valid")
else:
    print("num 4 in cell (6, 7) is Invalid")
    
if is_valid(board, 6, (1, 0)):
    print("num 6 in cell (1, 0) is valid")
else:
    print("num 6 in cell (1, 0) is Invalid")
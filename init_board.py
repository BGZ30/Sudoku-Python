import random
import linecache

def build_board():    
    filename = "5.txt"
    m = random.randint(0,10001)

    # retrieve specific line
    model = linecache.getline(filename, m)

    # reshape to 9x9 matrix
    sudoko_board = [[], [], [],[], [], [],[], [], []]
                   
    for r in range(9):
        for c in range(9):
            sudoko_board[r].append(int(model[c + 9*r]))
    
    return sudoko_board

'''print()
print(model)
print(sudoko_board)
'''
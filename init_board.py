import random
import linecache
    
filename = "5.txt"
m = random.randint(0,10001)

# retrieve specific line
model = linecache.getline(filename, 2)

# reshape to 9x9 matrix
sudoko_board = [[], [], [],[], [], [],[], [], []]
               
for r in range(9):
    for c in range(9):
        sudoko_board[r].append(model[c + 9*r])

'''print()
print(model)
print(sudoko_board)
'''
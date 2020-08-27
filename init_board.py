import random
import linecache
    
filename = "5.txt"
m = random.randint(0,10000)

# retrieve specific line
model = linecache.getline(filename, m)
print (model)
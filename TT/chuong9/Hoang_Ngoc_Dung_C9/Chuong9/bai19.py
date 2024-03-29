import random
numbers = random.sample(range(1,10),9) 
cols    = random.sample(range(9),9)
rows    = random.sample(range(9),9)

print(numbers)
print(cols)
print(rows)
print("--------------------------------")

matrix = [[numbers[(r+c)%9] for c in cols] for r in rows]
for line in matrix: print(line)  

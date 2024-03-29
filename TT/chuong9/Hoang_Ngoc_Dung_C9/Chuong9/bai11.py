from random import randint

L = [[0] * 5 for i in range(5)]

for i in range(10):
    while True:
        row = randint(0, 4)
        col = randint(0, 4)
        if L[row][col] == 0:
            L[row][col] = 1
            break

for i in L:
    print(i)

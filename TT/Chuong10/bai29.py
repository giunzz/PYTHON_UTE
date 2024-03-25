import numpy as np
from random import randint


def caclute_bom(a):
    dd = [(0,1), (0,-1), (-1,0), (1,0), (-1,1), (-1,-1), (1,1), (1,-1)]
    n = len(a)
    for i in range(n):
        for j in range(n):
            if (a[i][j] == -1): continue
            for k in range (len(dd)):
                x = i + dd[k][0]
                y = j + dd[k][1]
                if (x >= 0 and x < n and y >= 0 and y < n and a[x][y] == -1):
                    a[i][j] += 1
    return a
if __name__ == "__main__":
    print("play Minesweeper game")
    n = 5
    a = np.zeros((n,n), dtype = int)
    for i in range(0,n):
        for j in range(0,n):
            x = randint(0,1)
            a[i][j] = int(randint(-1,0)) 
    print(a)
    print("--------------------------------")
    print (caclute_bom(a))
    
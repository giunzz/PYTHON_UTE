from random import randint
from pprint import pprint
import numpy as np

# def check_row(a,n):
#     s = sum(a[0][0:(n-1)])
#     for i in range(1,n):
#         if s != sum(a[i][0:(n-1)]): return False
#     return True
    
    
# def check_colum(a):
#     s = sum(a[0:(n-1)][0])
#     for i in range(1,n):
#         if s != sum(a[0:(n-1)][i]): return False
#     return True

def prinma(a):
    print("--------------------------------")
    for i in range(3):
        for j in range(3):
            print(a[i][j], end = " ")
        print("")
        
def check_Magic_square(a,n,s):
    for i in range(n):
        if s != sum(a[i][0:n]): 
            return False
    for j in range(n):
        t = 0
        for i in range(n):
            t += a[i][j]
        if s != t:
            return False
    # for i in range(n):
    #     if s != sum(a[i][i]): return False
    # for i in range(n):
    #     if s != sum(a[i][n-1-i]): return False
    return True

if __name__ == '__main__':
    # n = 4
    # a = []
    # for i in range(0, n * n):
    #     a.append(randint(1,5))
    # L = np.array(a).reshape(n,n).tolist() # covert series to list
    # for i in range(n):
    #     print(L[i])
    # if (check_colum == 1 and check_row == 1): print("magic square")
    # else : print("Not magic square")
    a = [[5,1,9],[7,6,2],[3,8,4]]
    print(len(a))
    if (check_Magic_square(a,len(a),15) == 1):  prinma(a) 

    
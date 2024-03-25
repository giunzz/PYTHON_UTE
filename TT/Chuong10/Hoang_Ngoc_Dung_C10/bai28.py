import numpy as np



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

def fill_maxtrix(a,s):
    print("Fill ALL Magic square numbers 3 x3: ")
    a[1][0] = s - a[1][1] - a[1][2]
    a[2][2] = s - a[2][1] - a[2][0]
    for i in range(0,11):
        x = i 
        y = s - a[0][0] - i
        a[0][1] = x
        a[0][2] = y
        if (check_Magic_square(a,len(a),s) == 1):  
            prinma(a) 
    
    

if __name__ == "__main__":
    n = 3
    a = [[5,0,0], [0,6,2] , [3,8,0]]
    prinma(a)
    s = int(n * (n * n + 1)/2)
    fill_maxtrix(a,s)
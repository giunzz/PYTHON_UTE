
def check(L):
    for i in range(5):
        for j in range(5):
            if L[i][j] == 0: return False
    return 1


from random import randint

if __name__ == '__main__':
    n = 5
    a = []

    for i in range(0, n):
        a.append([])
        for j in range(0, n):
            a[i].append(randint(0,1))
    for i in range(0, n):
        for j in range(0, n):
            print(a[i][j], end=' ')
        print()
    ans = 0
    while(check(a) == 0):
        ans += 1
        print("--------------------------------")
        for i in range(0, n):
            for j in range(0, n):
                print(a[i][j], end=' ')
            print()
            x = randint(0,4) 
            y = randint(0,4)
            a[x][y] = 1
    print("Checking the number of times the program runs: ", ans)
    for i in range(0, n):
        for j in range(0, n):
            print(a[i][j], end=' ')
        print()
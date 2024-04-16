def check(n):
    if (n <= 1): return 0
    for i in range(2, n):
        if (n % i == 0): return 0
    return 1

if __name__ == '__main__':
    n = int(input("Nhap mot so: "))
    if (check(n)): print(str(n) + " la so nguyen to")
    else : print(str(n) + " khong phai so nguyen to")
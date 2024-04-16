def check(n):
    if (n % 2 == 0): return 1
    else: return 0

if __name__ == '__main__':
    n = int(input("Nhap mot so: "))
    if (check(n)): print(str(n) + " la so chan")
    else : print(str(n) + " la so le")
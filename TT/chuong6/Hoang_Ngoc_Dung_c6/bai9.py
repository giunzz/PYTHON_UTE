#exercise 9
def choi():
    x = int(input("Nhập một số: "))
    for i in range(1, x + 1):
        print(" " * (i - 1) + str(i))
if __name__ == "__main__":
    choi()

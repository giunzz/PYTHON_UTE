#exercise 12
def a():
    n = input("Nhập một từ: ")
    s = ''.join(char.lower() if i % 2 == 0 else char.upper() for i, char in enumerate(n))
    print(s)

if __name__ == "__main__":
    a()

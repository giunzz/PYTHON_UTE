#exercise 17
def g():
    for i in range(26):
        for j in range(26):
            print(chr((i + j) % 26 + ord('a')), end='')
        print()

if __name__ == "__main__":
    g()

def printP(n):
    for line in range(1,n+1):
        for i in range(line):
            print(line, end ="")
        print(" "*(20-line*2), end = ' ')
        for i in range(line): 
            print(line - i , end="")
        print('')


printP(5)


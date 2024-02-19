print('EX 13.print an upside down triangle')
n = 4
for i in range(n):
    for j in range(0, n - i):
        print("*", end=" ")
    print(' ')
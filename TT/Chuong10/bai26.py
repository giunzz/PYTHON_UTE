user = int(input("Enter your number: "))
for i in range(1,1001):
    for j in range(1,1001):
        tmp = i * i - j * j
        # if tmp > user : break
        if tmp == user: print(i,j)
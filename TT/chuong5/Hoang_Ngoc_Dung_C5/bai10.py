import numpy as np 
m =[]
print("Enter 10 test score")
sum = 0
for i in range(10):
    flag = 1
    while flag:
        n = int(input("Enter the score: "))
        if (n <= 1000): 
            m.append(n)
            flag = 0
            sum += n
print("Lowest test score: ", min(m))
print("Highest test score: ", max(m))
print("Average test score: ", sum/10)
m.sort()
sum = sum - m[0] - m[1]
print("New average test score: ", sum/8)



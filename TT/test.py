import random
n = 4
prob = 0.1
check = 0
for i in range(n):
    for j in range(n):
        num = random.random() < prob
        if (num == 1):
            check += 1
# => Xác suất < 50 % 
print(check/(n*n) , check, n*n)   
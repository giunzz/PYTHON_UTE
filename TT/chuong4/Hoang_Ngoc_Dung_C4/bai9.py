n = int(input("Enter a number: "))
print("All the divisors: ", end = " ")
for i in range(1,n):
    if (i * i == n) :break
    if (n % i == 0): print(i , end = " ")
print(n)
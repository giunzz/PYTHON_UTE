n = int(input("Enter a number: "))
s = 0
for i in range(1,n + 1):
    if (n % i == 0): s += i
print("The sum of the divisors of a number: ", s)
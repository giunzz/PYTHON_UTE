n = int(input("Enter a number: "))
s = 1
print(str(n)+ "!", end = " = ")
for i in range(1,n + 1):
    s *= i
    print (i , end =" * ")
print("\b\b = ", s)
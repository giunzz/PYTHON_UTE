# Write a program to determine how many of the numbers between 1 and 10000 contain the
# digit 3.
s=0
for i in range(1,10001):
    if '3' in str(i):
        s+=1

print(s)
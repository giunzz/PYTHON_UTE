from math import sqrt

num = int(input('Please enter your number to compute the square root: '))

ans = 1
while abs(sqrt(num)-ans) > 0.0000000001:
    ans = (ans + (num/ans))/2

print(ans)
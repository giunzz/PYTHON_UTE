from bai6 import sumab

a = 4
b = 19
print(sumab(a,b))

import numpy as np

def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return abs(x)


x = int(input('enter a number: '))
g = x
for i in range(4):
    x = int(input('enter a number: '))
    g = computeGCD(g,x)
print('GCD of these numbers: ',g)
import math
def check(x):
    t = math.sqrt(x)
    if ( t * t == x): return True
    else : return False


n = int(input("Enter a number: "))
flag = 0
for i in range (2,n + 1):
    if (n % i == 0 and check(i)):
        print("Not squarefree")
        flag = 1
        break
if (flag == 0): print("Squarefree")
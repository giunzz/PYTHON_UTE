
n = 1000
t = 1
for i in range(1,n + 1):
    t *= i
t = str(t)
s = 0
for i in range(len(t)-1,0, -1):
    if (t[i] == '0'): s += 1
    else : break
print("1000! ends with zero:", s)

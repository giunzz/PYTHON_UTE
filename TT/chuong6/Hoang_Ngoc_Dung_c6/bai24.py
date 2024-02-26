s = input("ENter a calculus: ")
s = '0'+ s 
s = list(s)
num1 = 0
num2 = 0
t = ""
for i in s:
    if i == 'x': break
    t += i
num1 = eval(t)
if (num1 == 0): num1 = 1
t1 = ""
for i in range(len(s)-1, 0 ,-1):
    if s[i] == '^': break
    t1 += s[i]
t1 = t1[::-1]
num2 = int(t1)

print(num2 * num1, "x^", num2-1, sep = "")

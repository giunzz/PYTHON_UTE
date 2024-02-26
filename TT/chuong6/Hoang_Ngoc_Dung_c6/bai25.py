s = input("ENter a calculus: ")
s = list(s)

def check_num(u):
    if (u == " " or u == 'x' or u == 'y' or u == '+'):
        return 0
    if (eval(u) >= 0 and int(u) <= 9):
        return True
    return False
def check(t):
    if (t == 'x' or t == 'y'):
        return 1
    return 0

for i in range(0,len(s)):
    if (check_num(s[i-1]) and check(s[i])): print("*" + s[i], end="")
    else: print(s[i], end="")

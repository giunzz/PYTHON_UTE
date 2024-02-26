from random import randint
user = input("enter a string: ")
s = list(user)
dd = [0] * len(user)
sz = 0
tmp = ''
while sz != len(user):
    while(1):
        i = randint(0, len(user) - 1)
        if (dd[i] == 0):
            dd[i] = 1
            tmp = tmp + s[i]
            sz += 1
            break
        
print(tmp)
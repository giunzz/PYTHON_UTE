import math
print("a)")
user = input("Enter a message: ")
user = list(user)
t = ""
t2 = ""
for i in range(0,len(user), 2): 
    t += user[i]
for i in range(1,len(user), 2): t2 += user[i]
print("New message: ", t + t2)

print("b)")
str = "msaeesg"
str = list(str)
t = ""
t2 = ""
for i in range(0,len(str),2): t += str[i]
for i in range(1,len(str),2): t2 += str[i]
l = list(t + t2)
l = l[-1:] + l[:-1]
t= ""
for i in range(len(l)): t += l[i]
print("Decryte: ", t)





print("EX1: ")
print(" Hoang Ngoc Dung \n" * 100)
print("EX2: ")
print(" Hoang Ngoc Dung " * 100)
print("EX3: ")
for i in range(1,101):
    print(i , " Hoang Ngoc Dung")
print("EX4: ")
for i in range(1,21):
    print(i,i * i , sep = " --- ")
print("EX5: ")
for i in range(8, 90,3):
    print(i,end = " ")
print("")
print("EX6:\r")
for i in range(100, 0,-2):
    print(i,end = " ")
print()
print("EX7:")
print("A" * 10 +  "B"* 7 +  "CD" * 5+  "E" + "F"*6 + "G")

print("EX8:")
name = (input("Enter your name: "))
times = int(input("How many times to print it: "))
for i in range(times):
    print(name)
    
    
print("EX9:")
n = int(input("Enter the number: "))
t1 = 1 
t2 = 1
if (n == 1) : print(t1)
else: 
    print(t1, end = " ")
    print(t2, end = " ")
    for i in range(3, n + 1):
        print(t1 + t2, end = " ")
        c  = t1 + t2
        t1 = t2
        t2 = c
print("\r")
print('EX 10. Print a box like the one below')
s = 19
for i in range(4):
    print(" ".join("*"*s))
print('EX 11. Print a box like the one below')
print(" ".join("*"*s))
for i in range(0, 2):
    print("* "+"  "*(s-2) + "*")
print(" ".join("*"*s))
print('EX 12.Print a triangle like the one below')
n = 4
for i in range(n):
    for j in range(0, i + 1):
        print("*", end=" ")
    print(' ')
print('EX 13.print an upside down triangle')
n = 4
for i in range(n):
    for j in range(0, n - i):
        print("*", end=" ")
    print(' ')
print('14.  print a diamond like the one below')
n = 9

for a1 in range(1, (n+1)//2 + 1): #from row 1 to 5
    for a2 in range((n+1)//2 - a1):
        print(" ", end = "")
    for a3 in range((a1*2)-1):
        print("*", end = "")
    print()

for a1 in range((n+1)//2 + 1, n + 1): #from row 6 to 9
    for a2 in range(a1 - (n+1)//2):
        print(" ", end = "")
    for a3 in range((n+1 - a1)*2 - 1):
        print("*", end = "")
    print()



print('15. prints a giant letter A like the one below')
h = int(input("Enter the height of the letter A: "))
print(" " * (h+1) + "*")
for i in range(h - 1):
    if (i != h // 2 - 1): print(" " * (h - i)+ "*" + " " * (2 * i + 1) + "*" )
    else: print(" " * (h - i) + "*" * (2 * i + 2) + "*" )

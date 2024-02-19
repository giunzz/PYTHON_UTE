    
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
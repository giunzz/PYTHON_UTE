from random import randint
print("10 Multiplication questions: ")
for i in range(10):
    a = randint(1,10)
    b = randint(1,10)
    n = a * b
    user = int(input(str(a) + " x " + str(b) + " = "))
    if (user == n): print("Right")
    else: print("Wrong. The answer is ", n , ".")


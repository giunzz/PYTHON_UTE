from random import randint
ques = int(input("How many questions do you want to do? "))
print(" Multiplication questions: ", ques)
correct = 0
for i in range(ques):
    a = randint(1,10)
    b = randint(1,10)
    n = a * b
    user = int(input(str(a) + " x " + str(b) + " = "))
    if (user == n): 
        print("Right")
        correct += 1
    else: print("Wrong. The answer is ", n , ".")
print("Player got correct answers: ", correct, " out of ", ques, " questions.")


from random import randint
print("You have five numbers to get")
s = 0
for i in range (5):
    x = int(input("Enter a number: "))
    n = randint(1,10)
    if (x == n): s += 10
    else: s -= 1
print("Your score is: ", s)
    

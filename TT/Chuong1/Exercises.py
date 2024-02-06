print('EX 1. Print a box like the one below')
s = 19
for i in range(4):
    print(" ".join("*"*s))
print('EX 2. Print a box like the one below')
print(" ".join("*"*s))
for i in range(0, 2):
    print("* "+"  "*(s-2) + "*")
print(" ".join("*"*s))
print('EX 3.Print a triangle like the one below')
n = 4
for i in range(n):
    for j in range(0, i + 1):
        print("*", end=" ")
    print(' ')
print('EX 4. prints the result: ', end= "")
t = (512 - 282) / ( 47 * 48 + 5)
print('%.4f' % t)

print('EX 5')
x = int(input("Enter a number: "))
print('The square of', x, 'is', str(x*x) + '.', sep=" ")

print('EX 6')
x = int(input("Enter a number: "))
print (x,2 * x,3 * x, 4 * x , 5 * x, sep ="---")

print('EX 7')
x = float(input("Enter a weight in kiligrams: "))
print('Convert to pounds:', x*2.2)

print ('EX 8')
a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))
total = a + b + c
average = total / 3
print('The total of', a, b, c, 'is', total)
print('The average of', a, b, c, 'is', average)

print('EX 9')
bill = float(input("Enter the amount of a meal: "))
tip = float('Percent tip')
t = bill * tip / 100
print('The tip is: ', t, 'The total amount is: ', bill + t)





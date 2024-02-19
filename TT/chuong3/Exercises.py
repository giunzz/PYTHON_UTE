@ -35,3 +35,111 @@ print("Covert angle to 0 and 360: ", n)
print("EX8: ")
minute = int(input("Enter number of seconds: "))
print(minute, " seconds is ", minute // 60, " minutes and ", minute % 60, " seconds")

print("EX 9:")
hour = int(input("Enter the hour between 1 and 12: "))
x = int(input(("How many hours ahead? ")))
print("New hour: ", (hour + x ) % 12 ,"o'clock")

print("EX 10:")
p = int(input("Enter a power: "))
p = pow(2,p)
print("Last digit of 2^p: ", p % 10)
print("Last two digits of 2^p: ", p % 100)

print("EX 11:")
x = float(input(("Enter a weight in kilograms: ")))
print(round(x * 2.2 , 1))

print("EX 12:")
n = int(input("Enter the number : " ))
t = 1
for i in range(1,n + 1):
    t *= i
print("The factorial of ", n, " is ", t)

print("EX 13:")
import math
n = int(input("Enter the number : " ))
print("Sine of ", n, " is ", round(math.sin(n)))
print("Cosine of ", n, " is ", round(math.cos(n)))
print("Tangent of ", n, " is ", round(math.tan(n)))

print("EX 14:")
import math
x = int(input("Enter an angle in degrees: "))
print("The sine of ", x, " is ", round(math.sin(math.radians(x)), 2))

print("EX 15:")
import math
for i in range(0,346,15):
    j = math.radians(i)
    print(i,"--- " , end =" " )
    print('%.4f'% math.sin(j), end =" ")
    print('%.4f' %math.cos(j))

print("EX 16:")

y = (input("Enter a year: "))
if (len(y) == 3):
    C = int(y[0] + 1)
else :
    C = int(y[0] + y[1])
    if (int (y[2] + y[3]) != 0): C = C + 1
m = ( 15 + C - (C // 4) - ((8*C + 13)// 25)) % 30
y = int(y)
n = (4 + C - C // 4) % 7
a = y % 4
b = y % 7
c = y % 19
d = (19*c + m) % 30
e = (2*a + 4*b + 6*d + n) % 7

k = [2,5,10,13,16,24,39]
if (d == 29 and e == 6): print("April 19")
else :
    if (d == 28 and e == 6):
        for i in k : 
            if (m == i):
                print("April 18")
                break
    else: 
        print("April ", d + e - 9, end = " ")
        print("or ", end =" ")
        print("March ", 22 + d + e)

print("EX 17:")
import calendar
Y = int(input("Enter a year: "))
print("A year is a leap year: ", calendar.isleap(Y))

print("EX 18:")
amt = float(input("amount of change less than: $1.00: "))

cents = int(amt*100)
print("amt: ", cents)

quarter = cents/25
cents -= quarter*25

dime = cents/10
cents -= dime*10

nickel = cents/5
cents -= nickel*5

penny = cents

print("quarter", quarter)
print("cents", cents)

print("EX 19:")
print("modular rectangles")
w = int(input("Enter a width: "))
h = int(input("Enter a height: "))
k = 0
for i in range(0, w):
    for j in range(0,h):
        print(k, end =" ")
        k = (k + 1) % 10 
    print(" ")
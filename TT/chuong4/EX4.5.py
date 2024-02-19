print("EX1: ")
flag = 0
while flag == 0:
    len = float(input("Enter a length in centimeters: "))
    if (len >= 0): 
        flag = 1
        print("Convert length to inches:" '%.4f' % (len * 0.39370))

print("EX2: ")
tem= float(input("Enter a temp: "))
k = input("Celsius or Fahrenheit (C/F): ")
if (k == 'C'): tem = tem * 9/5 + 32
else: tem = 5/9 * (tem - 32)
print("Convert temperature : ", tem)

print("EX3: ")
tem = float(input("Enter  a temperature in Celsius: "))
if (tem < -273.15): print(" the temperature is invalid")
elif (tem == -273.15): print(" the temperature is absolute 0")
elif(tem < 0): print("the temperature is below freezing")
elif (tem == 0): print("he temperature is at the freezing point")
elif (tem < 100): print("the temperature is in the normal range")
elif (tem == 100): print("the temperature is at the boiling point")
else : print("the temperature is above the boiling point")

print("EX4: ")
n = int(input("How many credits they have taken: "))
if (n <= 23): print("Freshman")
elif (n <= 53): print("sophomore")
elif (n <= 83): print("Junior")
else: print("seniors")

print("EX5: ")
from random import randint

n = randint(1,10)
user = int(input("Enter a number: "))
if (user == n): print("Right")
else: print("Not")

print("EX6: ")
n = int(input("how many items they are buying: "))
if (n < 10): print("Total cost: ", n * 12)
elif (n < 100): print("Total cost: ", 9 * 12 + (n - 9) * 10) 
else : print("Total cost: ", 9 * 12 + 99 * 10 + (n - 9 - 99) *  7)

print("Ex7: ")
s1 = float(input("Enter the first side: "))
s2 = float(input("Enter the second side: "))
if (abs(s1 - s2) == 0.001) : print("Close")
else: print("Not close")

print("Ex8: ")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0): print("Leap year")
else: print("Not leap year")

print("EX9: ")
n = int(input("Enter a number: "))
print("All the divisors: ", end = " ")
for i in range(1,n):
    if (i * i == n) :break
    if (n % i == 0): print(i , end = " ")
print(n)


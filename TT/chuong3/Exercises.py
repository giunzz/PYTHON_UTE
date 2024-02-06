from random import randint

print("EX1: ")
for i in range(50): print(randint(3,6), end = " ")

print("EX2: ")
x = randint(1,50)
y = randint(2,5)
print(pow(x, y))

print("EX3: ")
name = "Hoang Ngoc Dung"
x = randint(1,10)
for i in range(x): print(name)

print("EX4: ")
x = randint(100,1000)/100
print(x)

print("EX5: ")
for i in range(2,52):
    print(randint(1,i), end =" ")

print("EX6: ")
x = float(input("Enter the number X: "))
y = float(input("Enter the number Y: "))
t = abs(x - y) / (x + y)
print(t)

print("EX7: ")
n = float(input("Enter an angle between -180 and 180: "))
n %= 360
print("Covert angle to 0 and 360: ", n)
    
print("EX8: ")
minute = int(input("Enter number of seconds: "))
print(minute, " seconds is ", minute // 60, " minutes and ", minute % 60, " seconds")

len = float(input("enter the length: "))
DV = int(input("Enter the unit of length: 1 for inches, 2 for feet, 3 for yards, 4 for miles, 5 for millimeters, 6 for centimeters, 7 for meters, 8 for kilometers: "))
choices = int(input("Convert from feet into inches(1), yards(2), miles(3), millimeters(4), centimeters(5),meters(6), or kilometers(7): "))
l = []
u = [12,0.333,  0.018939, 304.8, 30.48, 3.2808, 3280.8]
for i in range(1,8):
    for j in range(1,8):
        l.append(len * u[i-1] / u[j-1])
print(l[choices])
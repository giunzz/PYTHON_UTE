feet = float(input("enter the length in feet: "))
choices = int(input("Convert from feet into inches(1), yards(2), miles(3), millimeters(4), centimeters(5),meters(6), or kilometers(7): "))
l = []
l.append(feet * 12)
l.append(feet * 0.333)
l.append(feet * 0.018939)
l.append(feet * 304.8)
l.append(feet *30.48)
l.append(feet / 3.2808)
l.append(feet / 3280.8)
print(l[choices])

x = float(input("Marks of subject 1: "))
y = float(input("Marks of subject 2: "))
z = float(input("Marks of subject 3: "))

average = (x + y + z) / 3
print ("Average: ", average)
print("{0:.3f}".format(average)) 
print('%.3f' % average) 
n = int(input("Enter the number of house: "))
a = dict()

for i in range(n):
    x = int(input("Enter latitude " + str(i+1) + ": "))
    y = int(input("Enter the longitude " + str(i+1) + ": "))
    a.update({x:y})
    
print("House:")
print("The dictionary in a sorted order (house): ", sorted(a.items()))
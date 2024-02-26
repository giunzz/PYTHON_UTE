l = eval(input("Enter list having numbers between 1 & 12: "))

for i in range(len(l)):
    if l[i] > 10:
        l[i] = 10

print("List after removing numbers greater than 10:")
print(l)
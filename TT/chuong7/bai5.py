s1 = input("Select
           ")
l = eval(input("Enter list list of strings: "))
l2 = []
for i in range(len(l)):
    l2.append(l[i][1:])

print("List after removing first characters:")
print(l2)

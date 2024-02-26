l1 = eval(input("Enter list having numbers : "))
l2 = eval(input("Enter list having numbers : "))
L = []
for i  in range(len(l1)):
    L.append(l1[i] + l2[i])
print(L)

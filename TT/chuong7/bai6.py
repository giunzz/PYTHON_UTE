print("A list onsisting of the integers 0 through 49: ", end ="")
L = []
for i in range(0,50):
    L.append(i)
print(L)
print("A list containing the squares of the integers 1 through 50 ", end =" ")
L = []
for i in range(0,50):
    L.append(i * i)
print(L)

print("A list: ", end =" ")
L = []
j = 1
for i in range(ord('a'),ord('z')+1):
    L.append(chr(i) * j)
    j += 1
print(L)

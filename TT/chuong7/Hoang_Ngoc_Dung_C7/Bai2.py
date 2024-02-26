n = 20
from random import randint
L = []
for i in range(n):
    L.append(randint(1,100))
print("Print the list: ", L)
print("Print the average of the elements in the list: ", sum(L)/len(L))
print("Print the largest element in the list: ", max(L))
print("Print smallest element in the list: ", min(L))
L.sort()
print("Print the second largest in the list: ", L[-2])
print("Print the second smallest in the list: ", L[1])
sum = 0
for i in range(n):
    if (L[i] % 2 == 0): sum += 1
print("Print the number of even elements in the list: ", sum)
    





from bai8 import *
n = int(input("Enter the size of list: "))
L = []
for i in range(n):
    user = int(input("Enter a number: "))
    L .append(user)
print("Print the total number of items in the list: ", sum(L))
print("Print the last item in the list: ", L[-1])
print("Print the list in reverse order: ", L[::-1])
print("if the list contains a 5: ", "Yes" if 5 in L else "No")
print("Print the number of fives in the list: ", [a for (a,b) in enumerate(L) if b == 5])

del L[0]
del L[len(L) - 1]
L.sort()
print(L)

print("How many any integers in the list are less than 5: ", end =" ")
ans = 0
for i in L:
    if i < 5: ans += 1
print(ans)

s = input("Enter the a string: ")
l = list(s)
tmp = []
for i in range(len(l)):
    if l[i] in 'aeiouAEIOU': tmp.append(i) 
for i in range(len(l)):
    if i not in tmp: print(l[i], end ="")
l = eval(input('Enter the list: '))
print("Original List")
print(l)

l = l[-1:] + l[:-1]

print("Rotated List")
print(l)
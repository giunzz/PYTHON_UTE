
print('15. prints a giant letter A like the one below')
h = int(input("Enter the height of the letter A: "))
print(" " * (h+1) + "*")
for i in range(h - 1):
    if (i != h // 2 - 1): print(" " * (h - i)+ "*" + " " * (2 * i + 1) + "*" )
    else: print(" " * (h - i) + "*" * (2 * i + 2) + "*" )

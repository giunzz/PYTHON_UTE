print('EX 11. Print a box like the one below')
s = 5
print(" ".join("*"*s))
for i in range(0, 2):
    print("* "+"  "*(s-2) + "*")
print(" ".join("*"*s))
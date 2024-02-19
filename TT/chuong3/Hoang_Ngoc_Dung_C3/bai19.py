print("EX 19:")
print("modular rectangles")
w = int(input("Enter a width: "))
h = int(input("Enter a height: "))
k = 0
for i in range(0, w):
    for j in range(0,h):
        print(k, end =" ")
        k = (k + 1) % 10 
    print(" ")
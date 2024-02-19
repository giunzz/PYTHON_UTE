print("EX 16:")

y = (input("Enter a year: "))
if (len(y) == 3):
    C = int(y[0] + 1)
else :
    C = int(y[0] + y[1])
    if (int (y[2] + y[3]) != 0): C = C + 1
m = ( 15 + C - (C // 4) - ((8*C + 13)// 25)) % 30
y = int(y)
n = (4 + C - C // 4) % 7
a = y % 4
b = y % 7
c = y % 19
d = (19*c + m) % 30
e = (2*a + 4*b + 6*d + n) % 7

k = [2,5,10,13,16,24,39]
if (d == 29 and e == 6): print("April 19")
else :
    if (d == 28 and e == 6):
        for i in k : 
            if (m == i):
                print("April 18")
                break
    else: 
        print("April ", d + e - 9, end = " ")
        print("or ", end =" ")
        print("March ", 22 + d + e)

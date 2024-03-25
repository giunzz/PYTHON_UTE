# Here is an old puzzle you can solve using brute force by using a computer program to check all the possibilities: In the calculation 43 + 57 = 207, every digit is precisely one away from its true value. What is the correct calculation?

a = 43
b = 57
c = 207

list_2cs = [11, -11, 9, -9]
list_3cs = [111, -111, 109, 91, -91, 89, -89] 

for i in list_2cs:
    for j in list_2cs:
        for k in list_3cs:
            if (a + i) + (b + j) == c + k: 
                print(f"{a + i} + {b + j} = {c + k}")
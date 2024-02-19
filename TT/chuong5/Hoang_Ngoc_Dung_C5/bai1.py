s1 = 0
s4 = 0 
s9 = 0
for i in range(2,100):
    if (i * i > 100): break
    else: 
        if ((i*i) % 10 == 1): s1 = s1 + 1
        if ((i*i) % 10 == 4): s4 = s4 + 1
        if ((i*i) % 10 == 9): s9 +=  1
        
print("The squares of the numbers from 1 to 100 end in 1: ", s1)
print("The squares of the numbers from 1 to 100 end in 4: ", s4)
print("The squares of the numbers from 1 to 100 end in 9: ", s9)

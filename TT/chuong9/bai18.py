import random
number = random.sample(range(1,13),12)
l = number +[0 for i in range(36-12+1)]
random.shuffle(l)
lst=[]

for i in range(0,36,6):
    print(l[i:i+6])
    lst.append(l[i:i+6])
    

from random import randint
L =[]
for i in range(100):
    L.append(randint(0,100))
tmp =[]
tmp = tmp + max(L) * [0] + [1]
print("longest run of zeros: ", tmp, "is", max(L))

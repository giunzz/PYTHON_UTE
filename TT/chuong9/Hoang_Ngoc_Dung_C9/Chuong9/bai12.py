from random import randint

L = [randint(0, 1) for i in range(7)]
print(f'The list of entries when unchanged: {L} ')
i = 0
while i < 7:
    if L[i] == 0:
        L[i] = 1
        break
    else:
        i += 1
    
if i == 7:
    print("There are no nonzero entries")
else:
    print(f'The list after change: {L} ')
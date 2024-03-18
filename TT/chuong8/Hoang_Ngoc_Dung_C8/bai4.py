from random import shuffle
s = input("Enter the sentence :")
s = s.split()
shuffle(s)
t = ""
for i in range(len(s)):
    t = s[i] 
    x = t[0].upper() + t[1:]
    print(x, end = " ")       
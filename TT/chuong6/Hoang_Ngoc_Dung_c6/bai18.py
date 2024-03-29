s = input("Enter a string: ")
s = s.lower()
for i in range(ord('a'),ord('z')+1): 
    for j in s:
        check = 0
        if (i == j): check = 1
    if (check == 0): print(chr(i), end = " ")
print()
cnt = 0
id = 0
fi = 0
for i in range(len(s)):
    if s[i] == 'a' :
        cnt += 1
        if fi == 0: 
            id = i
            fi = 1
print("Ocurrences a letter: ", cnt, "First id: ", id + 1) 

x = ord('A') #65
y = chr(65) #A
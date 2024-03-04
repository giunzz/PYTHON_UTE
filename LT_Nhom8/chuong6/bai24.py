s = input("Enter the string: ")

flag = 0
for i in range(len(s)):
    if s[i] == 'n': 
        vt = i
        break
print("Extract the first n characters from the string: ",s[:vt -1] + s[vt + 1:])
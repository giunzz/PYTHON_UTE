s = input("Enter a string: ")
s = list(s.split(" "))
s.sort()

print("string lexicographic: ")
for i in s:
    print(i.strip())
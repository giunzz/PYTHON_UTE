s = input("Enter a string: ")
count = 1
for i in s:
    if i.isspace() == True : count += 1
print("Number of word: ", count)

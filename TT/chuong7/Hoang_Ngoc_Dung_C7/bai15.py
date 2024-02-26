a = {}
sh = 5
for i in range(ord('a'),ord('z')+1): 
    k = (i + sh - ord('a')) % 26
    print(chr(i), " ", chr(k + ord('a')))
    a[chr(i)] = chr(k)



messs = input("Emter the message: ")
messs = messs.lower().replace(" ", "")

for i in messs:
    if i.isalpha():
        print(a[i], end = "")

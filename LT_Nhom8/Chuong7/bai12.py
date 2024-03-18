n = 5
a = dict()

for i in range(n):
    name = input("Enter the name of author " + str(i+1) + ": ")
    ISBN = input("Enter the ISBN of author " + str(i+1) + ": ")
    a.update({name:ISBN})
tmp = a.copy()
print("The authors and their ISBNs: ", a)
print("Demonstrate the use of the clear() method: ",tmp.clear())
print("Demonstrate the use of the fromkeys() method: ")
for i in a: 
    print(tmp.fromkeys(i,0))
n = int(input("Enter the number of friends's names: "))
a = dict()

for i in range(n):
    name = input("Enter the name of friend " + str(i+1) + ": ")
    phone = input("Enter the phone number of friend " + str(i+1) + ": ")
    a.update({name:phone})
print("The dictionary in a sorted order: ", sorted(a.items()))
name = input("Enter the name of friend to check: ")
if name in a:
    print("The phone number of ", name, " is ", a[name])
else : 
    print("The name is not in the dictionary")
n = int(input("how many items they are buying: "))
if (n < 10): print("Total cost: ", n * 12)
elif (n < 100): print("Total cost: ", 9 * 12 + (n - 9) * 10) 
else : print("Total cost: ", 9 * 12 + 99 * 10 + (n - 9 - 99) *  7)

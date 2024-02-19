print("EX 18:")
amt = float(input("amount of change less than: $1.00: "))

cents = int(amt*100)
print("amt: ", cents)

quarter = cents/25
cents -= quarter*25

dime = cents/10
cents -= dime*10

nickel = cents/5
cents -= nickel*5

penny = cents

print("quarter", quarter)
print("cents", cents)

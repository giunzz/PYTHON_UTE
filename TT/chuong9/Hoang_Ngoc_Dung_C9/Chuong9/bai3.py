weight = int(input("enter the weight :"))
while weight < 0:
    print("invalid input: enter again " )
    weight = int(input("enter the weight :"))
pounds = round(float(weight) * 2.2046246262,3)
print('Your weight in pounds is', pounds)    

d = {}
while True :
    product_name = input(" enter the product name (or 'q' to quit):").lower()
    if product_name == 'q':
        break
    price = float(input(" enter the price' {product_name}'")) 
    d[product_name] = price

# lookups
while True:
    product_name =input("enter the product name (or 'q' to quit) :" )
    if product_name == 'q' :
        break
    if product_name in d:
        print(f"The price of '{product_name}' is ${d[product_name]:.2f}.")
    else :
        print(f'{product_name} is not found ')      
    
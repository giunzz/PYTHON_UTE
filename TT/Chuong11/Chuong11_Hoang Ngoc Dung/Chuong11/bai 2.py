d = {}
while True :
    product_name = input(" enter the product name (or 'q' to quit):").lower()
    if product_name == 'q':
        break
    price = float(input(" enter the price' {product_name}'")) 
    d[product_name] = price
while True:
    try:
      budget = float(input("Enter your budget: $"))
      if budget < 0:
        print("Error: Budget cannot be negative. Please enter a valid amount.")
        continue  
      break  
    except ValueError:
      print("Error: Invalid input. Please enter a numerical value for your budget.")
affordable_products = [product for product, price in d.items() if price < budget]

if affordable_products:
    print("Products under ${:.2f}:".format(budget))
    for product in affordable_products:
      print(f"- {product} (${d[product]:.2f})")
else:
    print(f"No products found under ${budget}.")
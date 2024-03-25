num_items = 10

prices =[]
products =[]

for i in range(num_items): 
    price = float(input(f'enter the price of the item {i+1} :'))
    product = input(f'enter the product of the item {i +1} :')
    prices.append(price)
    products.append(product)
discount_prices = [price * (1 - 0.11 ) for price in prices]
max_product_length=max(len(products) for product in products)
print('-' *(max_product_length + 14))
print(f"{'Product' :{max_product_length}} {'Price':>14}")

print('-' * (max_product_length + 14))
for i in range(num_items):
    print(f'{products[i]:<{max_product_length}} ${discount_prices[i]:.2f}')
print('-' * (max_product_length + 14))    




    
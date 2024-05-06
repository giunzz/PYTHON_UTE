class Product:

  def __init__(self, name, amount, price):
   
    self.name = name
    self.amount = amount
    self.price = price

  def get_price(self, number_to_buy):
    
    if number_to_buy < 10:
      # No discount for less than 10 items
      return number_to_buy * self.price
    elif 10 <= number_to_buy < 100:
      # 10% discount for 10 to 99 items
      discount = 0.1
    else:
      # 20% discount for 100 or more items
      discount = 0.2
    discounted_price = self.price * (1 - discount)
    return number_to_buy * discounted_price

  def make_purchase(self, number_to_buy):
    
    if number_to_buy > self.amount:
      raise ValueError(f"Insufficient stock. Only {self.amount} {self.name} available.")
    self.amount -= number_to_buy

# Example usage
product = Product("T-Shirt", 200, 14.7)

# Get the price for different purchase quantities
price_for_5 = product.get_price(5)
price_for_20 = product.get_price(20)
price_for_120 = product.get_price(120)

print(f"Price for 5 items: ${price_for_5:.2f}")
print(f"Price for 20 items: ${price_for_20:.2f}")  # Discounted price (10%)
print(f"Price for 120 items: ${price_for_120:.2f}")  # Discounted price (20%)

# Make a purchase
product.make_purchase(10)

print(f"Remaining stock: {product.amount}")
class Investment:
  

  def __init__(self, principal, interest):
    
    self.principal = principal
    self.interest = interest

  def value_after(self, years):
    
    return self.principal * (1 + self.interest / 100) ** years

  def __str__(self):
    return f"Principal - ${self.principal:.2f}, Interest rate - {self.interest:.2f}%"

# Example usage
investment = Investment(1000.0, 5.12)
print(investment)  # Output: Principal - $1000.00, Interest rate - 5.12%

# Calculate the value after 10 years
value_after_10_years = investment.value_after(10)
print(f"Value after 10 years: ${value_after_10_years:.2f}")
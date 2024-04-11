def binom(n, k):
  # Check for invalid inputs (negative n or k, or k > n)
  if n < 0 or k < 0 or k > n:
    return None  # Or raise an exception for invalid input

  # Handle common cases (n choose 0 and n choose n) efficiently
  if k == 0 or k == n:
    return 1

  # Use factorial function (assuming it's defined elsewhere)
  from math import factorial
  return factorial(n) // (factorial(k) * factorial(n - k))


result = binom(5, 2)
print(result)  
# Write a function that takes an integer n and returns a random integer with exactly n digits. For
# instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because
# that is really 93, which is a two-digit number

from random import randint
 
def random_n_digits(n):
    range_start = 10**(n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

print(random_n_digits(5))
#Use a list comprehension to produce a list that consists of all palindromic numbers between
#100 and 1000.

palindromic_numbers = [num for num in range(100, 1001) if str(num) == str(num)[::-1]]
print("Palindromic numbers between 100 and 1000:", palindromic_numbers)

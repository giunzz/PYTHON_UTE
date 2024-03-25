divisible_numbers =[]
for i in range(1000):
  if i % 7 == 0 and str(i)[-1] == "6":
    divisible_numbers.append(i)
print(f"Numbers between {1} and {1000} divisible by 7 and ending in 6: {divisible_numbers}")


def sum_digits(num):
  sum = 0
  if num < 0:
    num = abs(num)
  while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
  return sum

number = int(input(" enter the number: ")) 
result = sum_digits(number)
print(result) 
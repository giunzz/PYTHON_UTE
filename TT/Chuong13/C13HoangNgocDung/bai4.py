def sum_digit_root(num):
    while sum < 10: 
        sum = 0
        if num < 0:
            num = abs(num)
        while num > 0:
            digit = num % 10
            sum += digit
            num //= 10
 return sum

num = int(input(" enter the number: ")) 
result = sum_digit_root(num)
print(result) 
    
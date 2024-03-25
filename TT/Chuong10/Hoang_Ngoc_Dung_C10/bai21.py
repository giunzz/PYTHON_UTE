# Write a program that asks the user to enter a fraction in the form of a string like '1/2' or
# '8/24'. The program should reduce the fraction to lowest terms and print out the result.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

fraction_input = input("Enter a fraction want to reduce: ")
fraction_list = fraction_input.split('/')
numerator = int(fraction_list[0])
denominator = int(fraction_list[1])
num_reduce = gcd(numerator, denominator)

numerator = numerator // num_reduce
denominator = denominator // num_reduce

if denominator == 0:
    print("Please enter a valid denominator (not 0)")
elif numerator == 0:
    print(f"The fraction of reduction: 0")
else:
    print(f"The fraction of reduction: {numerator}/{denominator}")


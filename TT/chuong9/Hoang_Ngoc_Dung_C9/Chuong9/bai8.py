# The GCD (greatest common divisor) of two numbers is the largest number that both are divisible by. For instance, gcd(18, 42) is 6 because the largest number that both 18 and 42 are
# divisible by is 6. Write a program that asks the user for two numbers and computes their gcd.
# Shown below is a way to compute the GCD, called Euclid’s Algorithm.
# • First compute the remainder of dividing the larger number by the smaller number
# • Next, replace the larger number with the smaller number and the smaller number with
# the remainder.
# • Repeat this process until the smaller number is 0. The GCD is the last value of the larger
# number.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = gcd(num1, num2)
    print("The GCD of", num1, "and", num2, "is:", result)

if __name__ == "__main__":
    main()


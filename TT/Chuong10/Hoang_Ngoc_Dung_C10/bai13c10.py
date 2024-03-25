# The number 99 has the property that if we multiply its digits together and then add the sum
# of its digits to that, we get back to 99. That is, (9 × 9) + (9 + 9) = 99. Write a program to find
# all of the numbers less than 10000 with this property. (There are only nine of them.)

def calculate_sum_of_digits(number):
        return sum(int(digit) for digit in str(number))

def main():
    numbers_with_property = []
    for num in range(1, 10000):
        tich = 1
        for digit in str(num):
            tich *= int(digit)
        if tich + calculate_sum_of_digits(num) == num:
            numbers_with_property.append(num)
    
    print("Numbers less than 10000 with the described property:", numbers_with_property)

if __name__ == "__main__":
    main()

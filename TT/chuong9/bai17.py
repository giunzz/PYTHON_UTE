num = int(input("Enter a numerator : "))
de = int(input("Enter a denominator : "))
digit = int(input("Enter a digit want to know: "))
n = num/de
n = str(n)
print('Your digit is: ', n[digit + n.find('.')])
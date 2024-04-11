def cover_base20(n):
    #create
    digits =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
    base = 20
    result = ""
    while (n > 0):
        digit = n % base
        result = digits[digit] + result
        n //= base
    return result
if __name__ == '__main__':
    n = int (input('Enter a base 10 number: '))
    print("convert a base 10 number to base 20:", cover_base20(n))
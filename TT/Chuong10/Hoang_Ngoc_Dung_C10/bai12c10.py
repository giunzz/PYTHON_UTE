# The number 1961 reads the same upside-down as right-side up. Print out all the numbers between 1 and 100000 that read the same upside-down as right-side up.




def is_upside_down(number):
    upside_down_pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    upside_down_str = ''
    for digit in str(number):
        if digit not in upside_down_pairs:
            return False
        upside_down_str += upside_down_pairs[digit]
    return upside_down_str == str(number)[::-1]

def main():
    for num in range(1, 100001):
        if is_upside_down(num):
            print(num)

if __name__ == "__main__":
    main()


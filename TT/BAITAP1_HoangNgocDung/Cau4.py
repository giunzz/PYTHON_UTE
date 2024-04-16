import string


def check_digit(s):
    count = 0
    for i in s:
        if i in string.digits:
            count += 1
    return count

def check_a(s):
    count = 0
    for i in s:
        if i in string.ascii_letters:
            count += 1
    return count

if __name__ == '__main__':
    s = input("Nhap mot chuoi: ")
    print("So chu so trong chuoi: ", check_digit(s))
    print("So chu cai trong chuoi: ", check_a(s))

def check_am(s):
    thisset = set('aeiouAEIOU')
    return sum([1 for i in s if i in thisset])

if __name__ == '__main__':
    s = input("Nhap mot chuoi: ")
    print("so nguyen am trong chuoi:", check_am(s))
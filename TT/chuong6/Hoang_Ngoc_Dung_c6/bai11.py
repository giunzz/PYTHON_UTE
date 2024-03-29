#exercise 11





def tach_chuoi_tai_a():
    n = input("Nhập một từ chứa chữ 'a': ")
    vt = n.find('a')
    if vt != -1:
        print(n[:vt + 1])
        print(n[vt + 1:])
    else:
        print("Từ không chứa chữ 'a'.")

if __name__ == "__main__":
    s = input("Input string: ").split(" ")
    print(s)


#exercise 13
def ktrachuoi():
    chuoi_1 = input("Nhập chuỗi thứ nhất: ")
    chuoi_2 = input("Nhập chuỗi thứ hai: ")
    if len(chuoi_1) != len(chuoi_2):
        print("Hai chuỗi không có cùng độ dài.")
        return
    s = ''.join(a + b for a, b in zip(chuoi_1, chuoi_2))
    print(s)

if __name__ == "__main__":
    ktrachuoi()

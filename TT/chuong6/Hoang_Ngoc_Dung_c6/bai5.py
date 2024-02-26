#exercise 5
def kiemtra(user_string):
    # Kiểm tra xem chuỗi có đủ dài để thay đổi không
    if len(user_string) >= 2:
        new_string = user_string[0] + '*' + user_string[2:]
        new_string += '!!!'
        return new_string
    else:
        return "Chuỗi quá ngắn để thực hiện thay đổi."

def main():
    user_input = input("Nhập chuỗi của bạn: ")
    result_string = kiemtra(user_input)
    print("Chuỗi mới: ", result_string)

if __name__ == "__main__":
    main()

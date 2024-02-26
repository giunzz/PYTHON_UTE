#exercise 6
def process_string(user_string):
    lower_case_string = user_string.lower()
    cleaned_string = lower_case_string.replace('.', '').replace(',', '')

    return cleaned_string

def main():
    x = input("Nhập chuỗi của bạn: ")
    processed_string = process_string(x)
    print("Chuỗi sau xử lý: ", processed_string)

if __name__ == "__main__":
    main()

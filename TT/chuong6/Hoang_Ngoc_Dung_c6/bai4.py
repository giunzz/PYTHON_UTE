#exercise 4
def kiemtra(word):
    nguyen_am = set("aeiou")
    return any(char in nguyen_am for char in word.lower())

def main():
    x = input("Nhập một từ: ")
    co_nguyen_am = kiemtra(x)
    if co_nguyen_am:
        print("Từ này chứa nguyên âm.")
    else:
        print("Từ này không chứa nguyên âm.")

if __name__ == "__main__":
    main()

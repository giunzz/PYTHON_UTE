#exercise 7
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def main():
    x = input("Nhập một từ: ")
    if is_palindrome(x):
        print("Từ này là từ đối xứng.")
    else:
        print("Từ này không phải là từ đối xứng.")

if __name__ == "__main__":
    main()

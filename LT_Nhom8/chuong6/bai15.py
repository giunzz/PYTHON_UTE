def find(str, k):
    count = 0
    for i in range(len(str)):
        if str[i] == k:
            count += 1
    return count





def main():
    str = input("Enter a string: ")
    k = input("Enter a character: ")
    num = find(str, k)
    print(num)

if __name__ == "__main__":
    main()
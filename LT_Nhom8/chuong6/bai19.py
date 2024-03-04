def insert_(str,in_str,pos):
    return str[:pos] + in_str + str[pos:]

def main():
    str = input("Enter a string: ")
    in_str = input("Enter a string to insert: ")
    num = eval(input("Enter position: "))
    new_string = insert_(str, in_str, num)
    print(new_string)

if __name__ == "__main__":
    main()
num = input("Enter a phone number: ")

phone_number = list(num)

if len(phone_number) not in (12, 14) or not phone_number[0].isnumeric():
    print("Invalid")
else:
    if len(phone_number) == 12:
        valid_digits = [0, 1, 2, 4, 5, 6, 8, 9, 10, 11]

        for i in valid_digits:
            if not phone_number[i].isnumeric():
                print("Invalid")
                break
        else:
            print("Valid")
    else:  
        valid_digits = [0, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13]

        for i in valid_digits:
            if not phone_number[i].isnumeric():
                print("Invalid")
                break
        else:
            print("Valid")

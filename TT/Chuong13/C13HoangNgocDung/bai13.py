def change_case(s):
    text_out = ''
    for letter in s:
        if letter.isupper():
            text_out += letter.lower()
        else:
            text_out += letter.upper()
    print(text_out)

change_case('Duong duoNG')
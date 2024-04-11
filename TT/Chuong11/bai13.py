import string
all_letters= string.ascii_letters

def create_cipher(d,s):
    key = 4
    for i in range(len(all_letters)):   
        d[all_letters[i]] = all_letters[(i + key) % len(all_letters)]
    # print(d)
    cipher = ""
    for i in s:
        # print(i, d[i], type(d[i]))
        cipher += d[i]
    # print(cipher)
    return cipher

if __name__ == '__main__':
    s1 = input("Enter a string to encoded: ")
    s2 = input("Enter a string to check: ")
    d = dict()
    cipher = create_cipher(d,s1)
    if (cipher == s2): print(s2 + "is not an encoded version of" + s1)
    else : print(s2 + "is an encoded version of" + s1)
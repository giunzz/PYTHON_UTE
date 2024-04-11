def is_encoded_version(original, encoded):
    if len(original) != len(encoded):
        return False
    
    substitution_dict = {}
    
    for char1, char2 in zip(original, encoded):
        if char1 == char2:
            return False
        if char1 not in substitution_dict:
            substitution_dict[char1] = char2
        elif substitution_dict[char1] != char2:
            return False
    
    return len(set(substitution_dict.values())) == len(substitution_dict.values())

original_string = input("Enter the original string: ")
encoded_string = input("Enter the encoded string: ")

if is_encoded_version(original_string, encoded_string):
    print("The encoded string could be an encoded version of the original string.")
else:
    print("The encoded string is not an encoded version of the original string.")

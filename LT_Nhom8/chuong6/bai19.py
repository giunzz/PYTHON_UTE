# # def insert_(str,in_str,pos):
# #     return str[:pos] + in_str + str[pos:]

# # def main():
# #     str = input("Enter a string: ")
# #     in_str = input("Enter a string to insert: ")
# #     num = eval(input("Enter position: "))
# #     new_string = insert_(str, in_str, num)
# #     print(new_string)

# # if __name__ == "__main__":
# #     main()

# def up(s):
#     t = s[0].upper()
#     for i in range(1,len(s)):
#         if s[i-1] == ' ': t += s[i].upper()
#         else: t += s[i]
#     return t


# if __name__=='__main__':
#     s = input("Enter your name: ")
#     print("Your name is: ", up(s))
#     print("Charaters: ", len(s))
#     print("Words: ", len(s.split()))
#     print("Vowels: ", sum([1 for i in s if i in 'aeiouAEIOU']))
#     print("Consonants: ", sum([1 for i in s if i not in 'aeiouAEIOU']))


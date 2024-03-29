# . Recall that, given a string s, s.index('x') returns the index of the first x in s and an error
# if there is no x.
# (a) Write a program that asks the user for a string and a letter. Using a while loop, the
# program should print the index of the first occurrence of that letter and a message if the
# string does not contain the letter.
# (b) Write the above program using a for/break loop instead of a while loop.



def main():
    s = input("Enter a string: ")
    letter = input("Enter a letter to search for: ")
    
    index = -1
    for i in range(len(s)):
        if s[i] == letter:
            index = i
            break

    if index != -1:
        print(f"The first occurrence of '{letter}' is at index:", index)
    else:
        print(f"The string does not contain the letter '{letter}'.")

if __name__ == "__main__":
    main()


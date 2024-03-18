from random import choice

word = input('Enter a word: ')
letter_list = list(word)
anagram = []

for i in range(len(letter_list)):
    character = choice(letter_list)
    anagram.append(character)
    letter_list.remove(character)

ans = ''.join(anagram)
print(ans)

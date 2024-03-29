from random import choice

L = ["hello", "world", "python", "programming", "random", "language", "unique", "computer", "science", "algorithm"]

def check_repeat(word):
    flag = 0
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                flag = 1
                return True
    return False

while True:
    random_word = choice(L)
    if check_repeat(random_word) == True:
        continue
    else:
        print(f'A random word from the list that does not have any repeated letters: {random_word}')
        break






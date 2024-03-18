import random
words = ['Afghanistan', 'Danemark', 'VietNam','Canada', 'Hong-Kong', 'Island','Japan','Italy', 'Korea', 'Laos', 'Malaysia', 'Netherlands', 'Norway', 'Pakistan', 'Portugal', 'Singapore', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States', 'Uruguay', 'Venezuela', 'Zimbabwe']



if __name__ == '__main__':
    print('The Guess Game!!!')
    word = random.choice(words)
    turn = 5
    fail = 0
    guess = ''
    
    while(turn > 0):
        name = input('Guess the characters: ')
        guess += name
        fail = 0
        
        for char in word:
            if char in guess:
                print(char, end ="")
            else:
                print('_',end="")
                fail += 1
        print('')

        if fail == 0:
            print('You win')
            print('The word is: ', word)
            break
    
        
        
        if guess not in word:
            turn -= 1
            print('You have', + turn, 'more guesses')
            if turn == 0 :
                print('You lose')
                print('The word is: ', word)
    
    

import random
print("Monty Hall problem: ")
choice = int(input("How many doors do you want to play with? (3 or 4): "))

if (choice == 3): 
    print("Playing this game 1000 times")
    right = 0
    for i in range(1000):
        prizes = ['goat', 'car', 'goat']
        random.shuffle(prizes) 
        for i in range(len(prizes)):
            if (prizes[i] != 'car'):
                print("There is a goat behind door ", i + 1)
                break
        user = int (input("Which door do you want to choose? (1,2,3): "))
        # user = random.choice([1,2,3])
        for i in range(len(prizes)):
            if (prizes[i] == 'car'):
                if (i == user - 1): 
                    print("You win")
                    right += 1
                else: print("You lose")
    print("percentage of the time you would win by not switching: ", right/1000 * 100, "%")
else:
    right = 0
    print("Playing for four doors")
    prizes = ['goat', 'car', 'goat', 'goat']
    random.shuffle(prizes) 
    user = int (input("Which door do you want to choose? (1,2,3,4): "))
    vt =[]
    for i in range(len(prizes)):
        if (prizes[i] == 'car'): vt.append(i)
    for i in range(len(prizes)):
        if (prizes[i] != 'car'): vt.append(i)
        
    for i in range(len(prizes)):
        if (prizes[i] != 'car' and i != user - 1):
            print("There is a goat behind door ", i + 1)
            break
    c = input("Do you want to switch to door(y/n): ")
    if (c == 'y') :     
        user = int (input("Which door do you want to choose? (1,2,3,4): "))
        # user = random.choice([1,2,3])
    for i in range(len(prizes)):
        if (prizes[i] == 'car'):
            if (i == user - 1): 
                print("You win")
                right += 1
            else: print("You lose")

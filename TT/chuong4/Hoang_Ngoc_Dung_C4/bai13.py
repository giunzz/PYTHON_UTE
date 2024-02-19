from random import randint
m = ['Rock', 'Paper', 'Scissor']
print("There are five round play Rock-Paper-Scissor with Computer: ")
flag = 0
for i in range(5):
    computer = randint(0,2)
    user = int(input("Enter your choice Rock-Paper-Scissor (0/1/2): "))
    print("Computer choice: ", m[computer])
    print("Your choice: ", m[user])
    if (computer == user): print("Draw")
    if (computer == 0 and user == 1 or computer == 1 and user == 2 or computer == 2 and user == 0): 
        flag = flag + 1   
        print("You win this round " ,  i)
    else: print("You lose this round " , i)
if (flag > 2): print("You win the game")
else: print("You lose the game")
        

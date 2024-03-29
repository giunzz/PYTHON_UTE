from random import randint
score = 100

while score < 200 and score > 0:
    print("You have", score, "points.")
    ans = randint(0, 1)
    guess = int(input("Please enter your guess heads (1) or tails (0): "))
    if guess == ans:
        score += 9
    else:
        score -= 10
    if score < 0:
        print("You ran out of money!")
    elif score > 200:
        print("You got to 200!")


from random import sample

questions = [
    "What is the capital of France?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the largest planet in our solar system?",
    "What is the square root of 25?",
    "Which element has the chemical symbol 'H'?",
    "Who painted the Mona Lisa?",
    "What is the currency of Japan?",
    "What is the powerhouse of the cell?",
    "In which year did World War II end?",
    "What is the main ingredient in guacamole?"
]

answers = [
    "Paris",
    "William Shakespeare",
    "Jupiter",
    "5",
    "Hydrogen",
    "Leonardo da Vinci",
    "Yen",
    "Mitochondria",
    "1945",
    "Avocado"
]

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

question = sample(num, 4)
score = 0

for i in question:
    print("\nQuestion:", questions[i])

    user_answer = input("Your answer: ")

    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {answers[i]}")

print(f"\nYou got {score} out of 4 questions right.")

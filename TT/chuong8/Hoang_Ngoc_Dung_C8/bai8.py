from random import choice

names = input("Enter names separated by commas: ").split(',')
entries = [int(entry) for entry in input("Enter the corresponding entry count for each person: ").split(',')]


participants = []

for i in range(len(names)):
        participants.extend([names[i]] * entries[i])

winner = choice(participants)

print(f"The winner of the drawing is: {winner}")
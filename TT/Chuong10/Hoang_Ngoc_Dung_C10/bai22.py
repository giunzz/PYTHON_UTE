
solutions = []
flag = 0
for starfruit in range(21):
    for mango in range(34):
        orange = 100 -  starfruit - mango
        cost = 5*starfruit + 3*mango + (1/3)*orange
        if cost == 100:
            solutions.append([starfruit, mango, orange])

for i in solutions:
    print(f"Starfruits: {i[0]}, Mangoes: {i[1]}, Oranges: {i[2]}")


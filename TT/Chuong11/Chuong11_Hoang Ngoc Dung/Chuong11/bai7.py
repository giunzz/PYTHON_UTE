# Create a 5 × 5 list of numbers. Then write a program that creates a dictionary whose keys are
# the numbers and whose values are the how many times the number occurs. Then print the
# three most common numbers.



from random import randint
n = 5
grid = [randint(1, 5) for _ in range(n) for i in range(n)]
print(grid)
number_occurrences = {}
for num in grid:
    if num in number_occurrences:
        number_occurrences[num] += 1
    else:
        number_occurrences[num] = 1

sorted_occurrences = sorted(number_occurrences.items(), key=lambda x: x[1], reverse=True)
print("The three most common numbers are:")
for number, count in sorted_occurrences[:3]:
    print(f"Number: {number}, Occurrences: {count}")
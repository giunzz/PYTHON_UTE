import random
m = [[random.randint(1, 100) for i in range(10)] for i in range(10)]

for row in m:
    print(row)
largest_in_third_row = max(m[2])
smallest_in_sixth_column = min(row[5] for row in m)


print("\nLargest value in the third row:", largest_in_third_row)
print("Smallest value in the sixth column:", smallest_in_sixth_column)

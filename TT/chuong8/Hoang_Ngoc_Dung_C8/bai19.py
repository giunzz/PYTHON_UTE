checkerboard = [[1 if (i + j) % 2 == 0 else 2 for j in range(5)] for i in range(5)]

for row in checkerboard:
    print(row)

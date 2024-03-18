checkerboard = [[1 if (i + j) % 2 == 0 else 2 for j in range(8)] for i in range(8)]

for row in checkerboard:
    print(row)

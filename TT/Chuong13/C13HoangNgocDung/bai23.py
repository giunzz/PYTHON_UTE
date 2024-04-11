def is_valid_sudoku(board):
	rows = [set() for _ in range(9)]
	cols = [set() for _ in range(9)]
	subgrids = [set() for _ in range(9)]

	for i in range(9):
		for j in range(9):
			num = board[i][j]
			if num == 0:
				continue

			subgrid_index = (i // 3) * 3 + j // 3

			if num in rows[i] or num in cols[j] or num in subgrids[subgrid_index]:
				return False

			rows[i].add(num)
			cols[j].add(num)
			subgrids[subgrid_index].add(num)

	return True

import random
if __name__ == '__main__':
    n = 9
    board = []
    for i in range(n):
        tmp =[]
        for j in range(n):
            tmp.append(random.randint(0,9))
        board.append(tmp)
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    for i in range(n):
        for j in range(n):
            print(board[i][j],end = " ")
        print()
    if is_valid_sudoku(board):print("Valid")  
    else: print("Invalid")

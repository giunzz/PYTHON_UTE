
def isWinner(board, c):
	if (board[0] == c and board[1] == c and board[2] == c) or \
	(board[3] == c and board[4] == c and board[5] == c) or \
	(board[6] == c and board[7] == c and board[8] == c) or \
	(board[0] == c and board[3] == c and board[6] == c) or \
	(board[1] == c and board[4] == c and board[7] == c) or \
	(board[2] == c and board[5] == c and board[8] == c) or \
	(board[0] == c and board[4] == c and board[8] == c) or \
	(board[2] == c and board[4] == c and board[6] == c):
		return True

	return False


def isValid(board):
	xCount = 0
	oCount = 0
	for i in range(9):
		if board[i] == 'X':
			xCount += 1
		if board[i] == 'O':
			oCount += 1
	if xCount == oCount or xCount == oCount + 1:
		# Check if there is only one winner
		if isWinner(board, 'X') and isWinner(board, 'O'):
			return False

		# If 'X' wins, then count of X must be greater
		if isWinner(board, 'X') and xCount != oCount + 1:
			return False

		# If 'O' wins, then count of X must be same as oCount
		if isWinner(board, 'O') and xCount != oCount:
			return False

		return True

	return False

import numpy as np
import random
if __name__ == '__main__':
    
    n = 3
    board = []
    for i in range(n):
        for j in range(n):
            board.append(random.choice(['X', 'O', ' ']))
    x = random.randint(0,3)
    y = random.randint(0,3)
    while (board[x+y] != ' '):
        x = random.randint(0,3)
        y = random.randint(0,3)
    board[x+y] = random.choice(['X', 'O'])
    if isValid(board): print("Someone win")
    else: print("Someone lose")

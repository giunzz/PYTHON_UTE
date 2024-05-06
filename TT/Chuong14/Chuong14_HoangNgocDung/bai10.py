class Connect4:
    def __init__(self):
        self.board = [[' ']*7 for i in range(6)]
        self.player = 'X'
        self.winner = None

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('- '*7)

    def play(self):
        while not self.winner:
            self.print_board()
            col = int(input(f'Player {self.player}, enter the column (0->6): '))
            if not 0 <= col < 7:
                print('Invalid column!')
                continue
            if self.board[0][col] != ' ':
                print('Column is full!')
                continue
            row = 0
            while row < 5 and self.board[row+1][col] == ' ':
                row += 1
            self.board[row][col] = self.player
            if self.check_winner(row, col):
                self.winner = self.player
            self.player = 'O' if self.player == 'X' else 'X'
        self.print_board()
        print(f'Player {self.winner} wins!')

    def check_winner(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 4): # 4 oo xung quanh
                r, c = row + i*dr, col + i*dc
                if 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.player:
                    count += 1
                else:
                    break
            for i in range(1, 4):
                r, c = row - i*dr, col - i*dc
                if 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.player:
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False
Connect4().play()
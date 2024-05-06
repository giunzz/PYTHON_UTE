import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.player_wins = 0
        self.computer_wins = 0
        self.choices = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)

    def find_round_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'draw'
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'scissors' and computer_choice == 'paper') or \
            (player_choice == 'paper' and computer_choice == 'rock'):
            self.player_wins += 1
            return 'player'
        else:
            self.computer_wins += 1
            return 'computer'

    def check_game_winner(self):
        if self.player_wins > self.computer_wins:
            return 'player'
        elif self.player_wins < self.computer_wins:
            return 'computer'
        else:
            return 'draw'

    def play_round(self, player_choice):
        if self.current_round < self.rounds:
            self.current_round += 1
            computer_choice = self.get_computer_choice()
            round_winner = self.find_round_winner(player_choice, computer_choice)
            print(f"Round {self.current_round}: Player chose {player_choice}, Computer chose {computer_choice}.{round_winner.capitalize()} wins this round.") # capitalize() : in cho dep
            if self.current_round == self.rounds:
                game_winner = self.check_game_winner()
                print(f"Game over! The winner of the game is: {game_winner.capitalize()}")
        else:
            print("The game has already ended.")

n = 5
game = Rock_paper_scissors(n)
print("Welcome to Rock, Paper, Scissors!")
print("5 round:")    
for i in range(5):
    player_choice = input("Enter your choice (rock, paper, or scissors): ")
    game.play_round(player_choice)
    print()
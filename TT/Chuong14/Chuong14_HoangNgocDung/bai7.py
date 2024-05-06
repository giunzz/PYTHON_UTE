# Use the Standard_deck class of this section to create a simplified version of the game War.
# In this game, there are two players. Each starts with half of a deck. The players each deal
# the top card from their decks and whoever has the higher card wins the other player’s cards
# and adds them to the bottom of his deck. If there is a tie, the two cards are eliminated from
# play (this differs from the actual game, but is simpler to program). The game ends when one
# player runs out of cards

from random import shuffle

class StandardDeck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(2, 15):
                self.cards.append((value, suit))
    
    def shuffle(self):
        shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop(0)
    
    def add_cards(self, cards):
        self.cards.extend(cards)

class War:
    def __init__(self):
        self.deck = StandardDeck()
        self.deck.shuffle()
        self.player1_cards = []
        self.player2_cards = []
        self.deal_cards()
    
    def deal_cards(self):
        while len(self.deck.cards) > 1:
            self.player1_cards.append(self.deck.deal_card())
            self.player2_cards.append(self.deck.deal_card())
    
    def play_round(self):
        card1 = self.player1_cards.pop(0)
        card2 = self.player2_cards.pop(0)
        
        print(f"Player 1 plays: {card1}")
        print(f"Player 2 plays: {card2}")
        
        if card1[0] > card2[0]:
            print("Player 1 wins the round!")
            self.player1_cards.extend([card1, card2])
        elif card1[0] < card2[0]:
            print("Player 2 wins the round!")
            self.player2_cards.extend([card1, card2])
        else:
            print("It's a tie! Cards are discarded.")

        
        print(f"Player 1 has {len(self.player1_cards)} cards remaining.")
        print(f"Player 2 has {len(self.player2_cards)} cards remaining.")
    
    def play_game(self):
        flag = 1
        while (self.player1_cards and self.player2_cards) and flag == 1:
            self.play_round()
            print("Do you want to play again?")
            ans = int(input("Enter 1 to play again or 0 to exit: "))
            if ans == 1:
                flag = 1
            else:
                flag = 0

        if not self.player1_cards:
            print("Player 2 wins the game!")
        else:
            print("Player 1 wins the game!")


war_game = War()
war_game.play_game()
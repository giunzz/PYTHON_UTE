from random import sample

deck = [{'value': i, 'suit': c}
    for c in ['spades', 'clubs', 'hearts', 'diamonds']
    for i in range(2, 15)]

def deal_cards():
    return sample(deck, 3), sample(deck, 3)

def compare_cards(player1_cards, player2_cards):
    player1_values = sorted([card['value'] for card in player1_cards], reverse=True)
    player2_values = sorted([card['value'] for card in player2_cards], reverse=True)

    for value1, value2 in zip(player1_values, player2_values):
        if value1 > value2:
            return "Player 1 wins"
        elif value1 < value2:
            return "Player 2 wins"
    
    return "Draw"

player1_cards, player2_cards = deal_cards()

print("Player 1 cards:", player1_cards)
print("Player 2 cards:", player2_cards)

result = compare_cards(player1_cards, player2_cards)
print("Result:", result)

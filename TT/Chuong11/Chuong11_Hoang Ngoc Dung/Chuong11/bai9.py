from random import sample

deck = [{'value':i, 'suit':c}
    for c in ['spades', 'clubs', 'hearts', 'diamonds']
    for i in range(2, 15)]

def deal_three_cards(deck):
    return sample(deck, 3)

def is_flush(cards):
    suits = set(card['suit'] for card in cards)
    return len(suits) == 1

def is_three_of_a_kind(cards):
    values = [card['value'] for card in cards]
    return len(set(values)) == 1

def is_pair(cards):
    values = [card['value'] for card in cards]
    return len(set(values)) == 2

def is_straight(cards):
    cards.sort(key=lambda x: x['value'])
    values = [card['value'] for card in cards]
    return values[0] + 1 == values[1] and values[1] + 1 == values[2]

cards = deal_three_cards(deck)
print("Three cards dealt:", cards)

if is_flush(cards):
    print("Is flush")
if is_three_of_a_kind(cards):
    print("Is three of a kind")
if is_pair(cards):
    print("Is pair")
if is_straight(cards):
    print("Is straight")

suit_names = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven','Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
card_names = []
for value in card_values:
  for suit in suit_names:
    card_name = f"{value} of {suit}"
    card_names.append(card_name)
print(card_names)
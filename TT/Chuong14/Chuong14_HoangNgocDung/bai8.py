class CardGroup:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def next2(self):
        if len(self.cards) >= 2:
            return self.cards.pop(), self.cards.pop()
        else:
            return None


class SimpleDeck(CardGroup):
    def __init__(self):
        super().__init__()
        suits = ['Hearts', 'Spaces']
        for suit in suits:
            for value in range(2, 11):
                self.add_card((value, suit))


# Example usage
deck = SimpleDeck()
# print("Initial deck:", deck.cards)

top_two_cards = deck.next2()
print("Next two cards drawn:", top_two_cards)

# print("Remaining deck after drawing:", deck.cards)

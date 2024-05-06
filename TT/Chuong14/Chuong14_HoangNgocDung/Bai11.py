class Card:
    def __init__(self, cards):
        self.cards = cards

    def has_royal_flush(self):
        # possible straight (10, J, Q, K, A)
        return self.has_straight_flush(10, 11, 12, 13, 14)

    def has_straight_flush(self, *ranks):
        # Check for a straight flush with the given ranks
        return self.has_straight(ranks) and self.has_flush(ranks)

    def has_four_of_a_kind(self):
        # Check for four cards of the same rank
        for rank in set(card.rank for card in self.cards):
            if self.cards.count(rank) == 4:
                return True
        return False

    def has_full_house(self):
        ranks = [card.rank for card in self.cards]
        return len(set(ranks)) == 2 and ranks.count(ranks[0]) == 3 or ranks.count(ranks[1]) == 3

    def has_flush(self, ranks=None):
        if ranks is None:
            ranks = [card.rank for card in self.cards]
        return len(set(card.suit for card in self.cards if card.rank in ranks)) == 1

    def has_straight(self, ranks=None):
        if ranks is None:
            ranks = sorted(card.rank for card in self.cards)
        return len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4

    def has_three_of_a_kind(self):
        for rank in set(card.rank for card in self.cards):
            if self.cards.count(rank) == 3:
                return True
        return False

    def has_two_pair(self):
        # Check for two pairs of different ranks
        ranks = set(card.rank for card in self.cards)
        return len(ranks) == 3 and all(self.cards.count(rank) == 2 for rank in ranks)

    def has_pair(self):
        # Check for two cards of the same rank
        for rank in set(card.rank for card in self.cards):
            if self.cards.count(rank) == 2:
                return True
        return False

    def best(self):
        if self.has_royal_flush():
            return "Royal Flush"
        elif self.has_straight_flush():
            return "Straight Flush"
        elif self.has_four_of_a_kind():
            return "Four of a Kind"
        elif self.has_full_house():
            return "Full House"
        elif self.has_flush():
            return "Flush"
        elif self.has_straight():
            return "Straight"
        elif self.has_three_of_a_kind():
            return "Three of a Kind"
        elif self.has_two_pair():
            return "Two Pair"
        elif self.has_pair():
            return "Pair"
        else:
            return "High Card"
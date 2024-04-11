from random import sample

deck = [{'value': i, 'suit': c}
    for c in ['spades', 'clubs', 'hearts', 'diamonds']
    for i in range(2, 15)]

def is_flush(cards):
    suits = set(card['suit'] for card in cards)
    return len(suits) == 1

num_trials = 100000
flush_count = 0

for i in range(num_trials):
    hand = sample(deck, 5)
    if is_flush(hand):
        flush_count += 1

probability_flush = flush_count / num_trials
print("Estimated probability of being dealt a flush in a five card hand:", probability_flush)

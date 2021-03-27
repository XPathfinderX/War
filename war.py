import random

# Shuffle the cards.
# Split the cards in half.
# Make two decks, one with each half.

class Card:

    def __init__(self, suit, rank, name):
        self.suit = suit
        self.rank = rank
        self.name = str(name) + ' of ' + suit


class Deck:

    def __init__(self, cards):
        self.cards = cards    

    def count_cards(self):
        return len(self.cards)


def create_cards():
    ranks = list(range(2, 15))
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    names = ranks[:9] + ['Jack', 'Queen', 'King', 'Ace']
    cards = []
    for suit in suits:
        for index,rank in enumerate(ranks):
            card = Card(suit, rank, names[index])
            cards.append(card)
    return cards


cards = create_cards()

random.shuffle(cards)

deck1 = cards[:26]
deck1 = Deck(deck1)
deck2 = cards[26:]
deck2 = Deck(deck2)
print(deck1.count_cards())
print(deck2.count_cards())

print(deck1.cards[0].name)
print(deck2.cards[0].name)




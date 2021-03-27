# Create a card class for 52 cards. 
# Create a list of numbers 2-14.
# Create another list with the four suits as strings.
# Create another list with the face vaules (Jack, Queen, King, Ace, 2-10), in order.

class Card:

    def __init__(self, suit, rank, name):
        self.suit = suit
        self.rank = rank
        self.name = str(name)
    

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
print(cards[0])
print(cards[0].name)
print(cards[0].rank)
print(cards[0].suit)
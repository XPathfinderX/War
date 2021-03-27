# Create a card class for 52 cards. 
# Create a list of numbers 2-14.
# Create another list with the four suits as strings.
# Create another list with the face vaules (Jack, Queen, King, Ace, 2-10), in order.

class Card:

    def __init__(self, suit, rank, name):
        self.suit = suit
        self.rank = rank
        self.name = str(name)
    
ranks = list(range(2, 15))
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
names = ranks[:9] + ['Jack', 'Queen', 'King', 'Ace']

print(ranks)
print(suits)
print(names)
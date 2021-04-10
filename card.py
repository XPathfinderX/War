
class Card:

    def __init__(self, suit, rank, name):
        self.suit = suit
        self.rank = rank
        self.name = str(name) + ' of ' + suit
    
    def beats(self, card):
        return self.rank > card.rank
    
    def ties(self, card):
        return self.rank == card.rank
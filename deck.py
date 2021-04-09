import random

class Deck:

    def __init__(self, cards):
        self.cards = cards    

    def count_cards(self):
        return len(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def add_cards(self, cards):
        random.shuffle(cards)
        self.cards.extend(cards)
import random
from card import Card
from player import Player
from deck import Deck
from turn import Turn


class Game:

    def __init__(self):
        cards = self.create_cards()
        random.shuffle(cards)
        deck1 = Deck(cards[:26])
        deck2 = Deck(cards[26:])
        self.player1 = Player("John", deck1)
        self.player2 = Player("Jane", deck2)
        
    def create_cards(self):
        ranks = list(range(2, 15))
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        names = ranks[:9] + ['Jack', 'Queen', 'King', 'Ace']
        cards = []
        for suit in suits:
            for index,rank in enumerate(ranks):
                card = Card(suit, rank, names[index])
                cards.append(card)
        return cards
    
    def print_status(self):
        print(f'{self.player1.name} has {self.player1.count_cards()} cards.')
        print(f'{self.player2.name} has {self.player2.count_cards()} cards.\n')

    def take_turn(self):
        turn = Turn(self.player1, self.player2)
        turn.print_result()
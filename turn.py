
class Turn:
    count = 0

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def print_result(self):
        self.__class__.count += 1
        card1 = self.player1.draw_card()
        card2 = self.player2.draw_card()
        cards = [card1, card2]
        print(f'{self.player1.name} drew {card1.name}.')
        print(f'{self.player2.name} drew {card2.name}.')
        if card1.beats(card2):
            print(f'{self.player1.name} wins this turn!\n')
            self.player1.add_cards(cards)
        elif card1.ties(card2):
            print('There was a tie! The cards in play will be removed from the game.\n')
        else:
            print(f'{self.player2.name} wins this turn!\n')
            self.player2.add_cards(cards)
    
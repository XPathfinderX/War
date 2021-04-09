
class Turn:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def print_result(self):
        card1 = self.player1.draw_card()
        card2 = self.player2.draw_card()
        cards = [card1, card2]
        print(f'{self.player1.name} drew {card1.name}.')
        print(f'{self.player2.name} drew {card2.name}.\n')
        if card1.beats(card2):
            print(f'{self.player1.name} wins this turn!')
            self.player1.add_cards(cards)
        else:
            print(f'{self.player2.name} wins this turn!')
            self.player2.add_cards(cards)
            
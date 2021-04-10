

class Player:
    
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def count_cards(self):
        return self.deck.count_cards()
    
    def draw_card(self):
        return self.deck.draw_card()

    def add_cards(self, cards):
        self.deck.add_cards(cards)
    
    def has_lost(self):
        return self.count_cards() == 0
    
#     def player_prompt(self):
#         prompt = input("Would you like to play a game of War? Press 'Y' to continue and 'N' to quit.")
#         if prompt == 'Y' or 'y':
#             print("Welcome to the game of war!")
#         elif prompt == 'N' or 'n':
#             print("Oh, join us next time then")

# Player.player_prompt()


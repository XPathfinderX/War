from game import Game

# Push branch to Github.
# Create a loop to take turns until either player has run out of cards. 


game = Game()
while not game.is_over():
    game.print_status()
    game.take_turn()

game.print_winner()




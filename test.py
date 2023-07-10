import optimized_gol as gol

# create a game of life with 10 rows and 10 columns
game = gol.Game(10, 10)

# set the cells that should be alive
game.set_alive(0, 0)
game.set_alive(0, 1)
game.set_alive(1, 0)
game.set_alive(1, 1)

# print the game of life
gol.print_Game_of_life_to_terminal(game)y
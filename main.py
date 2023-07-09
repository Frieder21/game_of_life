def main():
    import optimized_gol
    game_size = 2048
    game_of_life = optimized_gol.Game(game_width=game_size, game_height=game_size)
    # game_of_life.generate_random_map()

    game_of_life.toggle_cell(int(game_size / 2) + 16, int(game_size / 2) + 8)  # will generate:
    game_of_life.toggle_cell(int(game_size / 2) + 17, int(game_size / 2) + 8)  # . . . . .
    game_of_life.toggle_cell(int(game_size / 2) + 15, int(game_size / 2) + 9)  # . . # # .
    game_of_life.toggle_cell(int(game_size / 2) + 16, int(game_size / 2) + 9)  # . # # . .
    game_of_life.toggle_cell(int(game_size / 2) + 16, int(game_size / 2) + 10) # . . # . .
    optimized_gol.print_Game_of_life_to_terminal(game_of_life, display_width=48, display_height=16, max_gen=100,
                                                 x_self=int(game_size / 2),
                                                 y_self=int(game_size / 2),
                                                 auto_gen=True, coloring=True, show_gen=True)
    # will set up the terminal output and will generate 100 generations automatically

if __name__ == "__main__":
    main()

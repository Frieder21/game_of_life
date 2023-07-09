def main():
    import optimized_gol

    xy_location = [0, 0]
    game_size = 2048
    game_of_life = optimized_gol.Game(game_width=game_size, game_height=game_size)
    # game_of_life.generate_random_map()
    game_of_life.toggle_cell(int(game_size / 2) + 16, int(game_size / 2) + 8)
    game_of_life.toggle_cell(int(game_size / 2) + 17, int(game_size / 2) + 8)
    game_of_life.toggle_cell(int(game_size / 2) + 15, int(game_size / 2) + 9)
    game_of_life.toggle_cell(int(game_size / 2) + 16, int(game_size / 2) + 9)
    game_of_life.toggle_cell(int(game_size / 2) + 16, int(game_size / 2) + 10)

    for i in range(1000):
        game_of_life.print_map_terminal(display_width=48, display_height=16, max_gen=10000,
                                        x_self=int(game_size / 2 + xy_location[0]),
                                        y_self=int(game_size / 2 + xy_location[1]))
        game_of_life.next_generation()
    game_of_life.print_map_terminal(display_width=48, display_height=16, max_gen=10000,
                                    x_self=int(game_size / 2 + xy_location[0]),
                                    y_self=int(game_size / 2 + xy_location[1]))


if __name__ == "__main__":
    main()
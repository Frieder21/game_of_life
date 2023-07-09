import copy
import sys
import time

def clear_to_start(text):
    lines = text.split('\n')  # separate lines
    lines = lines[::-1]  # reverse list
    n_lines = len(lines)  # number of lines
    for i, line in enumerate(lines):  # iterate through lines from last to first
        sys.stdout.write('\r')  # move to beginning of line
        sys.stdout.write(' ' * len(line))  # replace text with spaces (thus overwriting it)
        if i < n_lines - 1:  # not first line of text
            sys.stdout.write('\x1b[1A')  # move up one line
    sys.stdout.write('\r')  # move to beginning of line again


class game_of_life:
    def __init__(self, game_width=256, game_height=256, save_gen_gen=False):
        self.optimize_status = None
        self.optimized_list_new = []
        self.optimized_list = []
        self.save_gen_gen = save_gen_gen
        self.gen_gen_count = 0
        self.saved_generations = {}
        self.game_width = game_width
        self.game_height = game_height
        self.map = [[False for y in range(self.game_height)] for x in range(self.game_width)]
        self.count_size = 3
        self.text = ""

    def is_cell_alive(self, x, y):
        if not(x < 0 or y < 0 or x >= self.game_width or y >= self.game_height):
            return self.map[x][y]
        return False

    def set_cell(self, x, y, alive):
        if not(x < 0 or y < 0 or x >= self.game_width or y >= self.game_height):
            self.map[x][y] = alive

    def toggle_cell(self, x, y):
        self.map[x][y] = not self.map[x][y]

    def check_rules(self, x, y):
        alive_count = 0
        if self.is_cell_alive(x - 1, y - 1):
            alive_count += 1
        if self.is_cell_alive(x, y - 1):
            alive_count += 1
        if self.is_cell_alive(x + 1, y - 1):
            alive_count += 1
        if self.is_cell_alive(x - 1, y):
            alive_count += 1
        if self.is_cell_alive(x + 1, y):
            alive_count += 1
        if self.is_cell_alive(x - 1, y + 1):
            alive_count += 1
        if self.is_cell_alive(x, y + 1):
            alive_count += 1
        if self.is_cell_alive(x + 1, y + 1):
            alive_count += 1
        return (self.is_cell_alive(x, y) and alive_count == 2) or alive_count == 3

    def is_optimize_good(self):
        if len(self.optimized_list_new) > 0:
            if not self.optimized_list_new[-1] == "40%":
                if len(self.optimized_list_new * self.count_size) < (self.game_width * self.game_height):
                    return True
                else:
                    self.optimized_list_new[-1] = "40%"
            return False
        else:
            return True

    def next_gen_gen_map_optimize(self, x, y):
        if not(x - 1 < 0 or y - 1 < 0 or x - 1 >= self.game_width or y - 1 >= self.game_height) and not [x - 1,
                                                                                                      y - 1] in self.optimized_list_new:
            self.optimized_list_new.append([x - 1, y - 1])
        if not(x < 0 or y - 1 < 0 or x >= self.game_width or y - 1 >= self.game_height) and not [x,
                                                                                              y - 1] in self.optimized_list_new:
            self.optimized_list_new.append([x, y - 1])
        if not(x + 1 < 0 or y - 1 < 0 or x + 1 >= self.game_width or y - 1 >= self.game_height) and not [x + 1,
                                                                                                      y - 1] in self.optimized_list_new:
            self.optimized_list_new.append([x + 1, y - 1])
        if not(x - 1 < 0 or y < 0 or x - 1 >= self.game_width or y >= self.game_height) and not [x - 1,
                                                                                              y] in self.optimized_list_new:
            self.optimized_list_new.append([x - 1, y])
        if not(x + 1 < 0 or y < 0 or x + 1 >= self.game_width or y >= self.game_height) and not [x + 1,
                                                                                              y] in self.optimized_list_new:
            self.optimized_list_new.append([x + 1, y])
        if not(x - 1 < 0 or y + 1 < 0 or x - 1 >= self.game_width or y + 1 >= self.game_height) and not [x - 1,
                                                                                                      y + 1] in self.optimized_list_new:
            self.optimized_list_new.append([x - 1, y + 1])
        if not(x < 0 or y + 1 < 0 or x >= self.game_width or y + 1 >= self.game_height) and not [x,
                                                                                              y + 1] in self.optimized_list_new:
            self.optimized_list_new.append([x, y + 1])
        if not(x + 1 < 0 or y + 1 < 0 or x + 1 >= self.game_width or y + 1 >= self.game_height) and not [x + 1,
                                                                                                      y + 1] in self.optimized_list_new:
            self.optimized_list_new.append([x + 1, y + 1])
        if not [x, y] in self.optimized_list_new:
            self.optimized_list_new.append([x, y])

    def next_generation(self):
        self.gen_gen_count += 1
        if not self.optimized_list:
            self.optimized_list_new = []
            done = False
            for x in range(self.game_width):
                for y in range(self.game_height):
                    if not self.is_optimize_good():
                        done = True
                        break
                    if self.is_cell_alive(x, y):
                        self.next_gen_gen_map_optimize(x, y)
                if done:
                    break
            self.optimized_list = copy.deepcopy(self.optimized_list_new)
            self.optimized_list_new = []
        next_gen_map = [[False for y in range(self.game_height)] for x in range(self.game_width)]
        self.optimize_status = self.is_optimize_good()
        if self.is_optimize_good():
            for x_y in self.optimized_list:
                if self.check_rules(x_y[0], x_y[1]):
                    next_gen_map[x_y[0]][x_y[1]] = True
                    if self.is_optimize_good():
                        self.next_gen_gen_map_optimize(x_y[0], x_y[1])
        else:
            for x in range(self.game_width):
                for y in range(self.game_height):
                    if self.check_rules(x, y):
                        next_gen_map[x][y] = True
                        if self.is_optimize_good():
                            self.next_gen_gen_map_optimize(x, y)
        self.map = next_gen_map
        self.optimized_list = copy.deepcopy(self.optimized_list_new)
        self.optimized_list_new = []
        if self.save_gen_gen:
            self.saved_generations[self.gen_gen_count] = self.map

    def print_map_terminal(self, display_width=None, display_height=None, x_self=None, y_self=None, show_gen=True,
                           max_gen=None, show_optimize_status=True):
        if max_gen is None:
            if show_optimize_status:
                last = " optimize status:" + str(self.optimize_status) + "\n"
            else:
                last = "\n"
        else:
            if show_optimize_status:
                last = "/" + str(max_gen) + " optimize status:" + str(self.optimize_status) + " " + str(len(self.optimized_list)) +"\n"
            else:
                last = "/" + str(max_gen) + "\n"
        if display_width is None:
            display_width = self.game_width
        if display_height is None:
            display_height = self.game_height
        if y_self is None:
            y_self = 1
        if x_self is None:
            x_self = 1
        if (not (self.text == "")) or self.gen_gen_count == 0:
            clear_to_start(self.text)
            if show_gen:
                self.text = "generation: " + str(self.gen_gen_count) + last
            else:
                self.text = ""
        for y in range(display_height):
            for x in range(display_width):
                if self.is_cell_alive(x + x_self, y + y_self):
                    self.text += "x "
                else:
                    self.text += ". "
            self.text += "\n"
        sys.stdout.write(self.text)
        sys.stdout.flush()

    def get_gen_gen_count(self):
        return self.gen_gen_count

    def get_optimized_list(self):
        return self.optimized_list

    def get_optimized_list_new(self):
        return self.optimized_list_new

    def get_optimize_status(self):
        return self.optimize_status

    def set_optimize_status(self, status):
        self.optimize_status = status

    def get_map(self):
        return self.map

    def get_game_width(self):
        return self.game_width

    def get_game_height(self):
        return self.game_height

xy_location = [0, 0]
game_size = 100
game_of_life2 = game_of_life(game_width=game_size, game_height=game_size)
#game_of_life.generate_random_map()
game_of_life2.toggle_cell(int(game_size / 2) + 16, int(game_size / 2) + 8)
game_of_life2.toggle_cell(int(game_size / 2) + 17, int(game_size / 2) + 8)
game_of_life2.toggle_cell(int(game_size / 2) + 15, int(game_size / 2) + 9)
game_of_life2.toggle_cell(int(game_size / 2) + 16, int(game_size / 2) + 9)
game_of_life2.toggle_cell(int(game_size / 2) + 16, int(game_size / 2) + 10)

for i in range(1000):
    game_of_life2.print_map_terminal(display_width=48, display_height=16, max_gen=1000,
                                    x_self=int(game_size / 2 + xy_location[0]),
                                    y_self=int(game_size / 2 + xy_location[1]))
    game_of_life2.next_generation()
game_of_life2.print_map_terminal(display_width=48, display_height=16, max_gen=1000,
                                    x_self=int(game_size / 2 + xy_location[0]),
                                    y_self=int(game_size / 2 + xy_location[1]))

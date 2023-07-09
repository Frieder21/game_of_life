import sys
import random
import copy
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

class Game:
    def update_map_size(self, game_width=None, game_height=None):
        if game_width is None:
            self.game_width = self.game_width
        else:
            self.game_width = game_width
        if game_height is None:
            self.game_height = self.game_height
        else:
            self.game_height = game_height
        self.map = [[0 for y in range(self.game_height)] for x in range(self.game_width)]

    def __init__(self, game_width=None, game_height=None, save_gen_gen=False):
        self.optimize_status = None
        self.optimized_list_new = []
        self.map = None
        self.optimized_list = []
        self.save_gen_gen = save_gen_gen
        self.gen_gen_count = 0
        self.saved_generations = {}
        if game_width is None:
            self.game_width = 8
        else:
            self.game_width = game_width
        if game_height is None:
            self.game_height = 8
        else:
            self.game_height = game_height
        self.update_map_size()
        self.count_size = 3
        self.text = ""
        self.count_map = [[[x - 1, y - 1] for x in range(self.count_size)] for y in range(self.count_size)]

    def is_cell_alive(self, x, y):
        if x - 1 < self.game_width and y - 1 < self.game_height and x > 0 and y > 0:
            if self.map[x - 1][y - 1] == 1:
                return True
            elif self.map[x - 1][y - 1] == 0:
                return False

    def count_cells(self, x, y):
        count = 0
        for x_self in self.count_map:
            for y_self in x_self:
                if self.is_cell_alive(x + y_self[0], y + y_self[1]) and not y_self == [0, 0]:
                    count += 1
        return count

    def toggle_cell(self, x, y):
        self.map[x - 1][y - 1] = int(not (bool(self.is_cell_alive(x, y))))

    def set_cell(self, x, y, alive):
        self.map[x - 1][y - 1] = int(alive)

    def check_rules(self, x, y):
        count = self.count_cells(x, y)
        alive = self.is_cell_alive(x, y)
        return (alive and count == 2) or count == 3

    def optimize_good(self):
        if len(self.optimized_list_new) > 0:
            if not self.optimized_list_new[-1] == "40%":
                if len(self.optimized_list_new*self.count_size) < (self.game_width*self.game_height):
                    return True
                else:
                    self.optimized_list_new[-1] = "40%"
                    return False
            else:
                return False
        else:
            return True

    def next_gen_gen_map_optimize(self, x, y):
        for x_self in self.count_map:
            for y_self in x_self:
                if not [x + y_self[0], y + y_self[1]] in self.optimized_list_new:
                    if x+1 < self.game_width and y+1 < self.game_height:
                        self.optimized_list_new.append([x + y_self[0], y + y_self[1]])

    def next_generation(self):
        self.gen_gen_count += 1
        if self.save_gen_gen:
            self.saved_generations[self.gen_gen_count] = self.map
        next_gen_map = [[0 for y in range(self.game_height)] for x in range(self.game_width)]
        if not self.optimized_list:
            self.optimized_list_new = []
            done = False
            for x in range(self.game_width):
                for y in range(self.game_height):
                    if not self.optimize_good():
                        done = True
                        break
                    if self.is_cell_alive(x + 1, y + 1):
                        self.next_gen_gen_map_optimize(x, y)
                if done:
                    break
            self.optimized_list = copy.deepcopy(self.optimized_list_new)
            self.optimized_list_new = []
        if self.optimized_list[-1] == "40%":
            self.optimize_status = False
            for x in range(self.game_width):
                for y in range(self.game_height):
                    if self.check_rules(x + 1, y + 1):
                        next_gen_map[x][y] = 1
                        if self.optimize_good():
                            self.next_gen_gen_map_optimize(x, y)
        else:
            self.optimize_status = True
            for x_y in self.optimized_list:
                if self.check_rules(x_y[0] + 1, x_y[1] + 1):
                    next_gen_map[x_y[0]][x_y[1]] = 1
                    if self.optimize_good():
                        self.next_gen_gen_map_optimize(x_y[0], x_y[1])
        self.map = next_gen_map
        self.optimized_list = copy.deepcopy(self.optimized_list_new)
        self.optimized_list_new = []

    def generate_random_map(self):
        for x in range(self.game_width):
            for y in range(self.game_height):
                self.set_cell(x, y, alive=bool(random.getrandbits(1)))

class print_Game_of_life_to_terminal:
    def update_last(self):
        self.optimize_status = self.game_of_life.optimize_status
        self.gen_gen_count = self.game_of_life.gen_gen_count
        if self.max_gen is None:
            if self.show_optimize_status:
                self.last = " optimize status:" + str(self.optimize_status) + "\n"
            else:
                self.last = "\n"
        else:
            if self.show_optimize_status:
                self.last = "/" + str(self.max_gen) + " optimize status:" + str(self.optimize_status) + "\n"
            else:
                self.last = "/" + str(self.max_gen) + "\n"

    def print_map_terminal(self):

        if (not (self.text == "")) or self.gen_gen_count == 0:
            clear_to_start(self.text)
            if self.show_gen:
                self.text = "generation: " + str(self.gen_gen_count) + self.last
            else:
                self.text = ""
        for y in range(self.display_height):
            for x in range(self.display_width):
                if self.is_cell_alive(x + self.x_self, y + self.y_self):
                    self.text += "x "
                else:
                    self.text += ". "
            self.text += "\n"
        sys.stdout.write(self.text)
        sys.stdout.flush()

    def auto_gen(self):
        self.max_gen = self.gen_gen_count + self.max_gen
        self.update_last()
        self.print_map_terminal()
        for i in range(self.max_gen - self.gen_gen_count):
            self.game_of_life.next_generation()
            self.update_last()
            self.print_map_terminal()


    def __init__(self, game_of_life, display_width=None, display_height=None, x_self=None, y_self=None, show_gen=True, max_gen=None, show_optimize_status=True, auto_gen=False):
        self.game_of_life = game_of_life
        self.optimize_status = self.game_of_life.optimize_status
        self.gen_gen_count = self.game_of_life.gen_gen_count
        self.last = ""
        self.text = game_of_life.text
        self.max_gen = max_gen
        self.show_optimize_status = show_optimize_status
        if display_width is None:
            self.display_width = game_of_life.game_width
        else:
            self.display_width = display_width
        if display_height is None:
            self.display_height = game_of_life.game_height
        else:
            self.display_height = display_height
        if y_self is None:
            self.y_self = 1
        else:
            self.y_self = y_self
        if x_self is None:
            self.x_self = 1
        else:
            self.x_self = x_self
        self.show_gen = show_gen
        self.is_cell_alive = game_of_life.is_cell_alive
        if auto_gen:
            self.auto_gen()
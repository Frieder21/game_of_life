# game of life

![gol_gui.jpg](https://beta.frieda-univers.me/static/assets/images/gol_gui.jpg)

## Introduction

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

## Rules

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated". Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## How I did it?

I created a python library that can be used to create a game of life. I also created a terminal frontend that can be used to see the game of life. The frontend uses the python library to create the game of life.

## How can I use it?

You can use the python library to create your own game of life. You can also use the terminal frontend to see the game of life.

![gol_code.jpg](https://beta.frieda-univers.me/static/assets/images/gol_code.jpg)

### First you need to install the python library in  your python project:

Download the python library from [here](https://github.com/Frieder21/game_of_life):
    
```bash
git clone https://github.com/Frieder21/game_of_life
```

Then you need to copy the library into your python project:

```bash
cp game_of_life/optimized_gol.py /path/to/your/python/project
cp game_of_life/Ansi_coloring.py /path/to/your/python/project
```

### Then you can use the library in your python project:

```python
import optimized_gol as gol

# create a game of life with 10 rows and 10 columns
game = gol.Game(10, 10)

# set the cells that should be alive
game.set_alive(0, 0)
game.set_alive(0, 1)
game.set_alive(1, 0)
game.set_alive(1, 1)

# print the game of life
gol.print_Game_of_life_to_terminal(game)
```

the output should look like this:

![gol_output.jpg](https://beta.frieda-univers.me/static/assets/images/gol_output.jpg)

## Where can I find the source code?

You can find the source code on [GitHub](https://github.com/Frieder21/game_of_life).


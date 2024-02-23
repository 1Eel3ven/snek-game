from tkinter import *
from random import randint

# ----------------------------------------- constants -----------------------------------

# sizes
GAME_WIDTH = 700
GAME_HEIGHT = 650
SPACE_SIZE = 50

#snake settings
SPEED = 100
BODY_PARTS = 3

# colors
SNAKE_COLOR = '#ffcc2f'
FOOD_COLOR = "#3096e2"
BG_COLOR = "#3e3e42"


# ------------------------------------ classes, funcs ------------------------------------

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS

        # snake position
        self.coordinates = []

        # stores body parts as squares
        self.squares = []


class Food:
    def __init__(self):
        # coords
        x = None
        y = None

        self.coordinates = (x, y)


# direction management

def next_move():
    pass

def change_direction(new_dir):
    pass


# game over funcs

def check_collisions(snake):
    pass

def game_over():
    pass
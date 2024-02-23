from tkinter import *
from random import randint

# ----------------------------------------- Constants -----------------------------------

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


# ------------------------------------ Classes, funcs ------------------------------------

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS

        # snake position
        self.coordinates = []

        # stores body parts as squares
        self.squares = []

        
        # initializing starting body parts
        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags='snake')
            self.squares.append(square)

class Food:
    def __init__(self):
        # separating the canvas into cells, and picking random cell
        x = randint(0, (GAME_WIDTH / SPACE_SIZE - 1)) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT / SPACE_SIZE - 1)) * SPACE_SIZE

        self.coordinates = (x, y)

        # oval with cell size
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags='food')


# direction management
        
def next_move():
    pass

    # we will add square in the beginning of move

    # if snake eats food in current move:
        # delete old food, generate new
    # else we will delete the square that we added

def change_direction(new_dir):
    pass


# game over funcs

def check_collisions(snake):
    pass

def game_over():
    pass


# ----------------------------------------- Main game --------------------------------------

# window settings
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

# default values
score = 0
dir = 'DOWN'


# screen settings
label = Label(window, text=f'Score: {score}', font=('comic-sans', 30))
label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BG_COLOR)
canvas.pack()

window.update() # !

# centering the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int(screen_width / 2) - int(window_width / 2)
y = int(screen_height / 2) - int(window_height / 2)

window.geometry(f'{window_width}x{window_height}+{x}+{y}')


snake = Snake()
food = Food()

window.mainloop()
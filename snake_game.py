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
        
def next_move(snake, food):
    x, y = snake.coordinates[0]

    # changing assigned coords based on direction

    if dir == 'UP':
        y -= SPACE_SIZE
    elif dir == 'DOWN':
        y += SPACE_SIZE
    elif dir == 'LEFT':
        x -= SPACE_SIZE
    elif dir == 'RIGHT':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    # adding a square
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags='snake')
    snake.squares.insert(0, square)

    # if snake eats food in current move:
        # delete old food, generate new
    # else we will delete the square that we added

    window.after(SPEED, next_move, snake, food)


def change_direction(new_dir):
    global dir
    # basically contradiction checking

    if new_dir == 'LEFT':
        if dir != 'RIGHT':
            dir = new_dir

    elif new_dir == 'RIGHT':
        if dir != 'LEFT':
            dir = new_dir
    
    elif new_dir == 'UP':
        if dir != 'DOWN':
            dir = new_dir
    
    elif new_dir == 'DOWN':
        if dir != 'UP':
            dir = new_dir


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

window.update()

# centering the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int(screen_width / 2) - int(window_width / 2)
y = int(screen_height / 2) - int(window_height / 2)

window.geometry(f'{window_width}x{window_height}+{x}+{y}')


# direction binds
window.bind('<Left>', lambda event: change_direction('LEFT'))
window.bind('<Right>', lambda event: change_direction('RIGHT'))
window.bind('<Up>', lambda event: change_direction('UP'))
window.bind('<Down>', lambda event: change_direction('DOWN'))


# The beginning of the game
snake = Snake()
food = Food()

next_move(snake, food)

window.mainloop()
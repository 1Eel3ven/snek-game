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


# some rank system for fun
def rank(score):
    if score < 6:
        return 'LOSER', '#8d0c13'
    elif 6 <= score < 11:
        return 'L', '#ed2b37'
    elif 11 <= score < 14:
        return 'Wanna ragequit??', '#eb1421'
    elif 14 <= score < 18:
        return 'DOG WATER', '#5bcefa'
    elif 18 <= score < 22:
        return 'GOOD', '#3db919'
    elif score >= 22:
        return 'KILLIN` IT!', '#83aeb9'
    elif score >= 27:
        return 'SSS', '#edcc19'


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

    
    if x == food.coordinates[0] and y == food.coordinates[1]:
        # if coordinates of food equal to snake`s head coordinates
        # then we update score and speed, delete food and make new
        global score, SPEED
        score += 1
        SPEED -= 3

        label.config(text=f'Score: {score} - {rank(score)[0]}')

        canvas.delete('food')
        food = Food()
    else:
        # if food wasnt eaten in current move, delete last square
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]


    if check_collisions(snake):
        game_over()
    else:
        # basically goes to another move after SPEED ms if no collisions
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
    x, y = snake.coordinates[0]

    # borders check
    if (x < 0 or x >= GAME_WIDTH) or (y < 0 or y >= GAME_HEIGHT):
        return True
    
    # checking if there`s no clash with tail
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False

def game_over():
    canvas.delete(ALL)
    user_rank = rank(score)

    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('comic-sans', 60), text=user_rank[0], fill=user_rank[1], tag='game_over')


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
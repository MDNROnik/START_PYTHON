import random
from tkinter import *

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 200
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.sq = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([50, 50])

        for x, y in self.coordinates:
            sq = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.sq.append(sq)


class Food:
    def __init__(self) -> object:
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    x, y = snake.coordinates[0]
    print((x, y))

    print("move ", direction)
    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    # insert new  part of the snake
    snake.coordinates.insert(0, (x, y))
    sq = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
    snake.sq.insert(0, sq)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score_level
        score_level += 1
        label.config(text="Score {}".format(score_level))
        canvas.delete("food")
        food = Food()
    else:
        # delete last part of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.sq[-1])
        del snake.sq[-1]

    if check_col(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text="GAME OVER", fill="red")


def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':

        if direction != 'up':
            direction = new_direction


def check_col(snake):
    x, y = snake.coordinates[0]
    print(x, y, GAME_HEIGHT, GAME_WIDTH)
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        # print(1111111111)
        return True
    for bp in snake.coordinates[1:]:
        if x == bp[0] and y == bp[1]:
            return True
    return False


window = Tk()
window.title("SNAKE GAME")
# window.resizable(False, False)
score_level = 0
direction = "down"

label = Label(window,
              text="Score: {}".format(score_level),
              font=('consolas, 40'))
label.pack()

canvas = Canvas(window,
                bg=BACKGROUND_COLOR,
                height=GAME_HEIGHT,
                width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# def click(window_width,window_height,screen_width,screen_height):
#     print(window_width,window_height,screen_width,screen_height)
# btn = Button(window, text="BTN", command=lambda :click(window_width,window_height,screen_width,screen_height) )
# btn.pack()

x = int((screen_width / 2) - (window_width / 2))

y = int((screen_height / 2) - (screen_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")  # position of the screen

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

food = Food()
snake = Snake()
next_turn(snake, food)

window.mainloop()

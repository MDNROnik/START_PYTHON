from tkinter import *
import random

value = 0
def next_turn(row, column):
    print(row, column)
    global player
    global value
    # print(("TURN ",value))
    player = players[value]
    # value ^= 1
    # print(buttons[row][column]['text'])

    # print(check_winner(), row, column)

    if buttons[row][column]['text'] == "" and check_winner() is False:

        buttons[row][column]['text'] = player
        if check_winner() is False:
            print(players[value])
            value ^= 1
            print(players[value])

            player = players[value]

            # print((value), player)
            label.config(text=(players[value] + " turn"))

        elif check_winner() is True:
            window.config(bg="green")
            label.config(text=(players[value] + " wins"))

        elif check_winner() == "Tie":
            window.config(bg="yellow")
            label.config(text="Tie!")

        # if player == players[0]:
        #
        #     buttons[row][column]['text'] = player
        #
        #     # print(buttons[row][column]['text'])
        #     if check_winner() is False:
        #         player = players[1]
        #         label.config(text=(players[1]+" turn"))
        #
        #     elif check_winner() is True:
        #         label.config(text=(players[0]+" wins"))
        #
        #     elif check_winner() == "Tie":
        #         label.config(text="Tie!")
        #
        # else:
        #
        #     buttons[row][column]['text'] = player
        #
        #     if check_winner() is False:
        #         player = players[0]
        #         label.config(text=(players[0]+" turn"))
        #
        #     elif check_winner() is True:
        #         label.config(text=(players[1]+" wins"))
        #
        #     elif check_winner() == "Tie":
        #         label.config(text="Tie!")

def check_winner():
    #print("hello")
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
           # print((1), buttons[row][0]['text'])
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            # print((2), buttons[0][column]['text'])
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        # print((3))
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        # print((4))
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player
    global value
    value = random.choice(zeroone)
    player = players[value]


    print(value," NEW ",player)

    label.config(text=player+" turn")
    window.config(bg="#F0F0F0")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
window.geometry("700x700")
players = ["x","o"]
zeroone = [0,1]
value = random.choice(zeroone)
player = players[value]
print((value),player)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

# print(type(buttons))
# buttons = [[0]*4]*4
#
# print(buttons)


# print(buttons,arr)
#
# print(type(buttons),type(arr))
label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for rows in range(3):
    for columns in range(3):
        buttons[rows][columns] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=rows, column=columns: next_turn(row,column))
        buttons[rows][columns].grid(row=rows,column=columns)

# print(type(buttons))

window.mainloop()
from tkinter import *



# window =Tk()
#
# canvas = Canvas(window,width=10,height=5, bg="red")
# canvas.pack()
#
#
#
# window.mainloop()

# def drag(event):
#     print(event)
#     lable.startX = event.x
#     lable.startY = event.y
# def drag2(event):
#     x = lable.winfo_x()-lable.startX+event.x;
#     y = lable.winfo_y() - lable.startY + event.y;
#     lable.place(x=x, y=y)
#
#
# window = Tk()
#
# lable = Label(window,bg="red", width=10, height=5)
# lable.place(x=0,y=0)
# lable.bind("<Button-1>", drag)
# lable.bind("<B1-Motion>", drag2)
#
#
# window.mainloop()

def click(num):
    print("you clicked the button")


def submit():
    user = entry.get()
    print(user)

window = Tk() #inistantiate an instance of a window

window.geometry("600x600") #window size

window.title("HELLO PYTHON ") #window title

# #icon change
# icon = PhotoImage(file='img.png')
# window.iconphoto(True,icon)
#
# window.config(background="white") #window backgroup color
#
# #label
# label = Label(window,
#               text="Hello Python GUI ",
#               fg="white",
#               background="green"
#               )
# label.pack()

#buttons
button = Button(window,
                text="click me",
                command=click(1),
                activeforeground="black",
                activebackground="red"
                )
button.pack()



# #entry
# entry =  Entry(window,
#                font=("Arial", 25),
#                )
# entry.pack()
# button = Button(window,
#                 text="click me",
#                 command=submit
#                 )
# button.pack()




window.mainloop() #place window on computer screen, listen for events

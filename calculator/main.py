from tkinter import *

now = 0
current = 0
pre = "+"
def button_pressed(num):
    global current
    global now
    global pre
    global equation_text
    #print(current, " ", now, " ", pre)
    if(type(num)==str):
        if(pre=="+"):
            now+=current
            current=0
            pre=num
        elif(pre=="-"):
            now -= current
            current = 0
            pre = num
        elif (pre == "/"):
            try:
                now /= current
                current = 0
            except ZeroDivisionError:
                equation_label.set("SyntaxError")
                equation_text = ""
        elif (pre == "*"):
            now *= current
            current = 0
            pre = num
    else:
        print(now,current)
        current = current * 10
        current+=num
        print(now,current)

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equal():

    try:
        global pre
        global now
        global current
        global equation_text
        print("HELLO")
        print(now, " ", pre, " ", current)

        if (pre == "+"):
            now += current
            current = 0
        elif (pre == "-"):
            now -= current
            current = 0
        elif (pre == "/"):
            print(now/current)
            try:
                now /= current
                current = 0
            except ZeroDivisionError:
                equation_label.set("SyntaxError")
                equation_text = ""
        elif (pre == "*"):
            now *= current
            current = 0


        equation_text = "" + str(now)
        equation_label.set(equation_text)
        current = 0
        pre = "+"
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("SyntaxError")
        equation_text = ""



def clear():
    global equation_text
    global pre
    global now
    global current
    pre="+"
    now=0
    current=0
    equation_text = ""
    equation_label.set(equation_text)


window = Tk()

window.title("Calculator Program")

window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window,
              textvariable=equation_label,
              font=('consolas', 20),
              bg="white",
              width=24,
              height=2
              )
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_pressed(1) ).grid(row=0, column=0)
button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_pressed(2) ).grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_pressed(3) ).grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_pressed(4) ).grid(row=1, column=0)
button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_pressed(5) ).grid(row=1, column=1)
button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_pressed(6) ).grid(row=1, column=2)
button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_pressed(7) ).grid(row=2, column=0)
button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_pressed(8) ).grid(row=2, column=1)
button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_pressed(9) ).grid(row=2, column=2)
button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_pressed(0) ).grid(row=3, column=0)

button_dot = Button(frame, text=".", height=4, width=9, font=35, command=lambda: button_pressed(".") ).grid(row=3, column=1)
button_equal = Button(frame, text="=", height=4, width=9, font=35, command=equal ).grid(row=3, column=2)

button_plus = Button(frame, text="+", height=4, width=9, font=35, command=lambda: button_pressed("+") ).grid(row=0, column=3)
button_min = Button(frame, text="-", height=4, width=9, font=35, command=lambda: button_pressed("-") ).grid(row=1, column=3)
button_divi = Button(frame, text="/", height=4, width=9, font=35, command=lambda: button_pressed("/") ).grid(row=2, column=3)
button_multi = Button(frame, text="*", height=4, width=9, font=35, command=lambda: button_pressed("*") ).grid(row=3, column=3)

button_clear = Button(window, text="Clear", height=4, width=9, font=35, command = clear ).pack()



window.mainloop()

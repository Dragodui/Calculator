from tkinter import *
from decimal import *
from math import *

root = Tk()
root["bg"] = "black"
root.title("Calculator")
root.geometry("350x350")
buttons = (
    ("7", "8", "9", "/", "DEL", "CE"),
    ("4", "5", "6", "*", "**", "10=>2"),
    ("1", "2", "3", "+", "%", "2=>10"),
    (".", "0", "=", "-",'sqrt','')
)
n = ""
name = "0"


def update():
    global name
    if name == "":
        name = "0"
    label.configure(text=name)


def calculate(operation):
    global name
    if operation == "CE":
        name = ''
    elif operation == "DEL":
        name = str(name[0:-1])
    elif operation == "sqrt":
        name = str(Decimal(sqrt(int(name))))
        name = name[0:6]
    elif operation == "=":
        name = str(eval(name))
    elif operation == "10=>2":
        b = ""
        while int(name) > 0:
            b = str(int(name) % 2) + b
            name = int(name) // 2
        name = b
    elif operation == "2=>10":
        name = int(name, base=2)
    else:
        if name == "0":
            name = ""
        name += operation
    update()


label = Label(root, font='30', bg="black", fg="white")
label.grid(row=1, columnspan=6, sticky="nsew")
root.rowconfigure(1, weight=4, minsize=0)

for row in range(4):
    root.rowconfigure(row + 2, weight=4, minsize=1)
    for col in range(len(buttons[row])):
        root.columnconfigure(col, weight=4, minsize=1)
        button = Button(root, text=buttons[row][col], fg="white", bg="black",activeforeground="black",
                        activebackground="white", font=20,
                        command=lambda row=row, col=col: calculate(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

root.mainloop()

from tkinter import *
memory = 0

# Button ka kaam
def click(event):
    global memory

    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(display.get())
            display.set(result)
        except:
            display.set("Error")

    elif text == "C" or text == "CE":
        display.set("")

    elif text == "⌫":
        display.set(display.get()[:-1])

    elif text == "%":
        try:
            number = float(display.get())
            display.set(number / 100)
        except:
            display.set("Error")

    elif text == "1/x":
        try:
            number = float(display.get())
            display.set(1 / number)
        except:
            display.set("Error")

    elif text == "x²":
        try:
            number = float(display.get())
            display.set(number ** 2)
        except:
            display.set("Error")

    elif text == "²√x":
        try:
            number = float(display.get())
            display.set(number ** 0.5)
        except:
            display.set("Error")

    elif text == "+/-":
        try:
            number = float(display.get())
            display.set(-number)
        except:
            display.set("Error")

    # Memory functions
    elif text == "MC":
        memory = 0

    elif text == "MR" or text == "M∨":
        display.set(memory)

    elif text == "M+":
        try:
            memory = memory + float(display.get())
        except:
            display.set("Error")

    elif text == "M-":
        try:
            memory = memory - float(display.get())
        except:
            display.set("Error")

    elif text == "MS":
        try:
            memory = float(display.get())
        except:
            display.set("Error")

    else:
        display.set(display.get() + text)


# Main window
root = Tk()
root.title("My Colorful Calculator")
root.geometry("400x550")
root.config(bg="#eeeeee")

# Display
display = StringVar()
display.set("")

screen = Entry(
    root,
    textvariable=display,
    font="Arial 28 bold",
    justify=RIGHT,
    bg="white",
    fg="#222222"
)

screen.pack(
    fill=X,
    padx=10,
    pady=12,
    ipady=10
)


# Memory buttons
memory_buttons = ["MC", "MR", "M+", "M-", "MS", "M∨"]

memory_colors = [
    "#ffcdd2",
    "#bbdefb",
    "#c8e6c9",
    "#ffe0b2",
    "#e1bee7",
    "#fff9c4"
]

memory_frame = Frame(root, bg="#eeeeee")
memory_frame.pack(fill=X, padx=5)

for i in range(len(memory_buttons)):

    b = Button(
        memory_frame,
        text=memory_buttons[i],
        font="Arial 10 bold",
        bg=memory_colors[i],
        fg="#333333",
        relief=RAISED
    )

    b.pack(
        side=LEFT,
        expand=True,
        fill=X,
        padx=2,
        pady=4
    )

    b.bind("<Button-1>", click)


# Calculator buttons
buttons = [
    ["%", "CE", "C", "⌫"],
    ["1/x", "x²", "²√x", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
]


# Button colors
colors = {
    "%": "#fff59d",
    "CE": "#ffccbc",
    "C": "#ffcdd2",
    "⌫": "#bbdefb",

    "1/x": "#b2ebf2",
    "x²": "#c8e6c9",
    "²√x": "#dcedc8",
    "/": "#ffcc80",

    "*": "#fff59d",
    "-": "#c8e6c9",
    "+": "#bbdefb",
    "=": "#aed581",

    "+/-": "#f8bbd0",
    ".": "#fff59d"
}


# Number buttons ke colors
number_colors = [
    "#d1c4e9",
    "#b2dfdb",
    "#f8bbd0"
]

number_count = 0


# Buttons banana
for row in buttons:

    frame = Frame(root, bg="#eeeeee")
    frame.pack()

    for item in row:

        if item.isdigit():
            bg_color = number_colors[number_count % 3]
            number_count += 1
        else:
            bg_color = colors.get(item, "#ffffff")

        b = Button(
            frame,
            text=item,
            width=5,
            height=1,
            font="Arial 18 bold",
            bg=bg_color,
            fg="#222222",
            relief=RAISED
        )










        b.pack(
            side=LEFT,
            padx=4,
            pady=4
        )

        b.bind("<Button-1>", click)


# Program run karna
root.mainloop()

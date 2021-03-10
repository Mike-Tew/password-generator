from tkinter import *


def generate_password():
    length = length_input.get()
    print(f"Generate {length}")

root = Tk()
root.title("Password Generator")

title_label = Label(
    root,
    width=20,
    height=2,
    text="Password Generator",
    font=("Helvetica 16 bold"),
    bg="#bfbfbf"
)
title_label.grid(row=0, column=0, columnspan=3)

length_label = Label(root, text="Length")
length_label.grid(row=1, column=0)

length_input = Spinbox(root, from_=1, to=10, font=("Helvetica 20"))
length_input.grid(row=1, column=1)

generate_button = Button(root, text="Generate", command=generate_password)
generate_button.grid(row=1, column=2)

password_display = Entry(root)
password_display.grid(row=2, column=0, columnspan=3)


root.mainloop()
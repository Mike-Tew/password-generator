from tkinter import Tk, END, Label, Spinbox, Button, Entry
from random import randint


def generate_password():
    """Generate a password based on the input length."""

    length = int(length_input.get())
    new_password = ""

    for _ in range(length):
        new_password += chr(randint(33, 125))

    password_display.delete(0, END)
    password_display.insert(0, new_password)


root = Tk()
root.title("Password Generator")

title_label = Label(
    root,
    width=23,
    height=2,
    text="Password Generator",
    font=("Helvetica 16 bold"),
    bg="#bfbfbf",
)
title_label.grid(row=0, column=0, columnspan=3, pady=[0, 30])

length_label = Label(root, text="Length:", font={"Helvetica 25"})
length_label.grid(row=1, column=0, sticky="e")

length_input = Spinbox(root, width=3, from_=1, to=15, font=("Helvetica", 20))
length_input.insert(1, 0)
length_input.grid(row=1, column=1)

generate_button = Button(
    root, text="Generate", font=("Helvetica 12"), command=generate_password
)
generate_button.grid(row=1, column=2, sticky="w")

password_display = Entry(
    root, width=15, font=("Helvetica 20"), bd=0, bg="systembuttonface", justify="center"
)
password_display.grid(row=2, column=0, columnspan=3, pady=[30, 0])

copy_button = Button(root, text="Copy to clipboard", font=("Helvetica", 12))
copy_button.grid(row=3, column=0, columnspan=3, pady=30)

root.mainloop()

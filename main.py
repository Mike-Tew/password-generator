from tkinter import *


def generate_password():
    length = length_input.get()
    password_display.delete(0, END)
    password_display.insert(0, f"Password length is {length}")

root = Tk()
root.title("Password Generator")

title_label = Label(
    root,
    width=23,
    height=2,
    text="Password Generator",
    font=("Helvetica 16 bold"),
    bg="#bfbfbf"
)
title_label.grid(row=0, column=0, columnspan=3, pady=[0, 30])

length_label = Label(root, text="Length:", font={"Helvetica 25"})
length_label.grid(row=1, column=0, sticky="e")

length_input = Spinbox(root, width=3, from_=1, to=10, font=("Helvetica 20"))
length_input.grid(row=1, column=1)

generate_button = Button(root, text="Generate", font=("Helvetica 12"), command=generate_password)
generate_button.grid(row=1, column=2, sticky="w")

password_display = Entry(root, width=15, font=("Helvetica 20"))
password_display.grid(row=2, column=0, columnspan=3, pady=[30, 40])

root.mainloop()

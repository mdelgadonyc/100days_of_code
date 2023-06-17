# Day 29 Project: Password Manager

import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(height=200, width=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
user_label = tkinter.Label(text="Email/Username:")
user_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

website_box = tkinter.Entry(width=35)
user_box = tkinter.Entry(width=35)
password_box = tkinter.Entry(width=21)

website_box.grid(column=1, row=1, columnspan=2, sticky="EW")
user_box.grid(column=1, row=2, columnspan=2, sticky="EW")
password_box.grid(column=1, row=3, sticky="EW")

generate_button = tkinter.Button(text="Generate Password")
add_button = tkinter.Button(text="Add", width=36, )

generate_button.grid(column=2, row=3, sticky="EW")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()

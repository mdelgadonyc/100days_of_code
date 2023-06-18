# Day 29 Project: Password Manager

import random
import tkinter
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_function():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_box.delete(0, "end")
    password_box.insert(0, password)
    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_box.get()
    email = user_box.get()
    password = password_box.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                              f"Password: {password}\nWould you like to save?")

        # All fields need to be cleared after Add button is pressed.
        website_box.delete(0, 'end')
        user_box.delete(0, 'end')
        user_box.insert(0, "user@email.com")
        password_box.delete(0, 'end')
        website_box.focus()

        if is_ok:
            # Write the data inside the entries to a data.txt file when the Add button is clicked.
            with open("data.txt", "a") as file:
                # Each website, email, and password combination should be on a new file line side the file.
                file.write(f"{website} | {email} | {password}\n")


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
website_box.focus()

user_box.grid(column=1, row=2, columnspan=2, sticky="EW")
user_box.insert(0, "mdelgadonyc@gmail.com")

password_box.grid(column=1, row=3, sticky="EW")

generate_button = tkinter.Button(text="Generate Password", command=generate_function)
add_button = tkinter.Button(text="Add", width=36, command=save)

generate_button.grid(column=2, row=3, sticky="EW")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
# add_button.bind("<Button-1>", save)

window.mainloop()

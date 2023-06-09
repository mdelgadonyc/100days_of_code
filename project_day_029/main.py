# Day 29 Project: Password Manager
import json
import random
import tkinter
from tkinter import messagebox
import pyperclip

FILENAME = "data.json"
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
    pyperclip.copy(password)


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

        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open(FILENAME, "w") as file:
                    json.dump(new_data, file)
            else:
                with open(FILENAME, "w") as file:
                    data.update(new_data)
                    json.dump(data, file, indent=4)
            finally:
                # All fields need to be cleared after Add button is pressed.
                website_box.delete(0, 'end')
                user_box.delete(0, 'end')
                user_box.insert(0, "user@email.com")
                password_box.delete(0, 'end')
                website_box.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_box.get()
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            password = data[website]["password"]
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists.")


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

website_box = tkinter.Entry(width=21)
user_box = tkinter.Entry(width=35)
password_box = tkinter.Entry(width=21)

website_box.grid(column=1, row=1, sticky="EW")
website_box.focus()

user_box.grid(column=1, row=2, columnspan=2, sticky="EW")
user_box.insert(0, "user@email.com")

password_box.grid(column=1, row=3, sticky="EW")

search_button = tkinter.Button(text="Search", command=find_password)
generate_button = tkinter.Button(text="Generate Password", command=generate_function)
add_button = tkinter.Button(text="Add", width=36, command=save)

search_button.grid(column=2, row=1, sticky="EW")
generate_button.grid(column=2, row=3, sticky="EW")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
# add_button.bind("<Button-1>", save)

window.mainloop()

# Day 31 Project: [Capstone] Flashy!

import random
import tkinter
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FILENAME = "data/french_words.csv"

dataframe = pd.read_csv(FILENAME)
word_list = dataframe.to_dict(orient="records")
LANGUAGE = dataframe.columns[0]
current_word = {}


# -------------------------- OBTAIN WORDS ----------------------------- #
def next_card():
    global current_word, flip_timer

    window.after_cancel(flip_timer)

    current_word = random.choice(word_list)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(word_text, text=current_word[LANGUAGE], fill="black")
    canvas.itemconfig(language, text=LANGUAGE, fill="black")

    flip_timer = window.after(3000, func=flip_card)


# --------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")

canvas = tkinter.Canvas(height=526, width=800, highlightthickness=0)
canvas.config(background=BACKGROUND_COLOR)
card_image = canvas.create_image(413, 270, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text=LANGUAGE, font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Create the two buttons
button_wrong_img = tkinter.PhotoImage(file="images/wrong.png")
button_right_img = tkinter.PhotoImage(file="images/right.png")

button_wrong = tkinter.Button(image=button_wrong_img, highlightthickness=0, command=next_card)
button_right = tkinter.Button(image=button_right_img, highlightthickness=0, command=next_card)

button_wrong.grid(column=0, row=1)
button_right.grid(column=1, row=1)

next_card()

window.mainloop()

# Day 31 Project: [Capstone] Flashy!

import random
import tkinter
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FILENAME = "data/french_words.csv"

dataframe = pd.read_csv(FILENAME)
word_list = dataframe.to_dict(orient="records")
LANGUAGE = dataframe.columns[0]


# -------------------------- OBTAIN WORDS ----------------------------- #
def get_word():
    current_word = random.choice(word_list)
    card_front.itemconfig(word_text, text=current_word[LANGUAGE])


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_front = tkinter.Canvas(height=526, width=800, highlightthickness=0)
card_front.config(background=BACKGROUND_COLOR)
card_front.create_image(413, 270, image=card_front_img)
card_front.grid(column=0, row=0, columnspan=2)

language = card_front.create_text(400, 150, text=LANGUAGE, font=("Ariel", 40, "italic"))
word_text = card_front.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Create the two buttons
button_wrong_img = tkinter.PhotoImage(file="images/wrong.png")
button_right_img = tkinter.PhotoImage(file="images/right.png")

button_wrong = tkinter.Button(image=button_wrong_img, highlightthickness=0, command=get_word)
button_right = tkinter.Button(image=button_right_img, highlightthickness=0, command=get_word)

button_wrong.grid(column=0, row=1)
button_right.grid(column=1, row=1)

get_word()

window.mainloop()

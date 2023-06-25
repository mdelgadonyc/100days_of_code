# Day 31 Project: [Capstone] Flashy!

import tkinter

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_front = tkinter.Canvas(height=526, width=800, highlightthickness=0     )
card_front.config(background=BACKGROUND_COLOR)
card_front.create_image(413, 270, image=card_front_img)
card_front.grid(column=0, row=0, columnspan=2)

language = card_front.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word = card_front.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Create the two buttons
button_wrong_img = tkinter.PhotoImage(file="images/wrong.png")
button_right_img = tkinter.PhotoImage(file="images/right.png")

button_wrong = tkinter.Button(image=button_wrong_img, highlightthickness=0)
button_right = tkinter.Button(image=button_right_img, highlightthickness=0)

button_wrong.grid(column=0, row=1)
button_right.grid(column=1, row=1)


window.mainloop()

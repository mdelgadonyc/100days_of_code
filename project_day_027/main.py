# Day 27 Project: Distance Converter GUI

import tkinter
import time

FONT = ("Arial", 20, "bold")

window = tkinter.Tk()
window.title("Tkinter GUI program")
window.config(padx=20, pady=20)


def miles_to_km():
    # convert miles to km

    miles = float(miles_input.get())
    km = miles * 1.609
    result_label["text"] = f"{km}"
    window.update()


# Entry
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

# Labels
miles_label = tkinter.Label(text="Miles", font=FONT)
# miles_label["text"] = "New Text"
# miles_label.config(text="New Text")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

equal_label = tkinter.Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text="0", font=FONT)
result_label.grid(column=1, row=1)

# Button
button1 = tkinter.Button(text="Calculate", command=miles_to_km)
button1.grid(column=1, row=2)


window.mainloop()

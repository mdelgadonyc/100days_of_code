# Day 25 Project: States Game

import turtle
import pandas

screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct = 0
correct_guesses = []

states_data = pandas.read_csv("50_states.csv")
list_of_states = states_data.state.to_list()
title = f"{correct}/50 States Correct"

# Use a loop to allow the user to keep guessing
while len(correct_guesses) < 50:

    # Obtain user guess and convert to Title case
    answer_state = screen.textinput(title=title, prompt="What's another state name? ")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in list_of_states:
            if state not in correct_guesses:
                missing_states.append(state)
            print(missing_states)
        break

    # Check if the guess is among the 50 states
    if answer_state in list_of_states:
        print(f"The guess {answer_state} is one of the 50 states")
        state_text = turtle.Turtle()

        # Write correct guesses onto the map
        matched_state = states_data[states_data.state == answer_state]
        x_coordinate = matched_state.x.iloc[0]
        y_coordinate = matched_state.y.iloc[0]
        state_text.penup()
        state_text.hideturtle()
        state_text.goto(x_coordinate, y_coordinate)
        state_text.write(answer_state)
        # Record the correct guesses in a list
        correct_guesses.append(matched_state)
        # Keep track of the score
        correct += 1

# states_to_learn.csv



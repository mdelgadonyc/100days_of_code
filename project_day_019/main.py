# Day 19 Project: Ready, Set, Turtle Power!

import random
from turtle import Turtle, Screen

screen = Screen()
start_y = -150
screen.setup(width=500, height=400)
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "gold", "green", "blue", "purple"]
turtles = []

# Create a turtle for each available color
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y)
    start_y += 60
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

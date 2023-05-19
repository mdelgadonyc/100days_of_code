# Day 18 Project: Magnifique!

import random
from turtle import Turtle,Screen, colormode

# Our Damien Hirst-inspired color palette
COLOR_LIST = [(198, 32, 12), (250, 17, 237), (39, 189, 77), (38, 68, 217), (238, 5, 227), (229, 45, 159),
              (27, 157, 39), (215, 12, 74), (15, 16, 154), (198, 11, 14), (243, 165, 33), (67, 30, 10), (229, 121, 17),
              (61, 8, 14), (225, 210, 141), (10, 61, 97)]
DOT_SIZE = 20
x_coor = -250
y_coor = -200

colormode(255)
tony = Turtle()
tony.speed("fastest")
screen = Screen()

tony.penup()
tony.setpos(x_coor, y_coor)


def get_random_color():
    new_color = random.choice(COLOR_LIST)
    return new_color


def draw_spot_row():
    for _ in range(10):
        new_color = get_random_color()
        tony.dot(DOT_SIZE, new_color)
        tony.forward(50)


def new_row_location():
    global y_coor
    y_coor += 50
    tony.setpos(x_coor, y_coor)


for _ in range(10):
    get_random_color()
    draw_spot_row()         # Draw a row of 10 spots
    new_row_location()      # Move starting point up by 50 paces and repeat draw_spot_row

tony.hideturtle()
screen.exitonclick()

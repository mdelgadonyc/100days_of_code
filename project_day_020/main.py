from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

kai = []

for index in range(3):
    square = Turtle(shape="square")
    square.penup()
    square.setpos(-(index*20), 0)
    square.color("white")
    kai.append(square)

# interlink the segments so that each one tracks the one in front
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(kai)-1, 0, -1):
        new_x = kai[seg_num-1].xcor()
        new_y = kai[seg_num-1].ycor()
        kai[seg_num].setpos(new_x, new_y)
    kai[0].forward(20)




screen.exitonclick()

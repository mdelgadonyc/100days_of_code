from turtle import Turtle
import time

# TODO: Create the ball and make it move
# self object to have w = 20, h = 20, at position 0,0

class Ball (Turtle):
    def __init__(self, position):
        super().__init__()
        self.bounce_value = 1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + (self.bounce_value * 10)
        self.goto(new_x, new_y)

    def bounce(self):
        self.bounce_value *= -1

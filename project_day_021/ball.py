from turtle import Turtle
import time

# TODO: Create the ball and make it move
# self object to have w = 20, h = 20, at position 0,0

class Ball (Turtle):
    def __init__(self, position):
        super().__init__()
        self.bounce_value_y = 1
        self.bounce_value_x = 1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + (self.bounce_value_x * 10)
        new_y = self.ycor() + (self.bounce_value_y * 10)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.bounce_value_y *= -1

    def bounce_x(self):
        self.bounce_value_x *= -1

    def restart(self):
        self.goto(0, 0)
        self.bounce_x()


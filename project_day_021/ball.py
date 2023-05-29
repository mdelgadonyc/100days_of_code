from turtle import Turtle

# Create the ball and make it move
# self object to have w = 20, h = 20, at position 0,0


class Ball (Turtle):

    def __init__(self, position):
        super().__init__()
        self.bounce_value_y = 1
        self.bounce_value_x = 1
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.speed_rate = 0.1

    def move(self):
        new_x = self.xcor() + (self.bounce_value_x * 10)
        new_y = self.ycor() + (self.bounce_value_y * 10)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.bounce_value_y *= -1
        self.speed_rate *= 0.9

    def bounce_x(self):
        self.bounce_value_x *= -1
        self.speed_rate *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.speed_rate = 0.1
        self.bounce_x()

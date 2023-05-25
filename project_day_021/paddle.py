from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.penup()
        self.goto(start_position)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def move_up(self):
        new_y = self.ycor()
        new_y += 20
        self.goto(self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor()
        new_y -= 20
        self.goto(self.xcor(), y=new_y)

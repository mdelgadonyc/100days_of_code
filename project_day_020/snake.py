from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.kai = []
        self.create_snake()
        self.head = self.kai[0]

    def create_snake(self):
        for index in range(3):
            square = Turtle(shape="square")
            square.speed("fastest")
            square.penup()
            square.setpos(-(index*20), 0)
            square.color("white")
            self.kai.append(square)

    def move(self):
        # interlink the segments so that each one tracks the one in front
        for seg_num in range(len(self.kai)-1, 0, -1):
            new_x = self.kai[seg_num-1].xcor()
            new_y = self.kai[seg_num-1].ycor()
            self.kai[seg_num].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


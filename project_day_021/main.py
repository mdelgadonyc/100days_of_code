# Day 21 Project: Pong-head

from turtle import Turtle, Screen

P1_START = (350, 0)

#TODO: Create the screen
screen = Screen()
screen.title("Welcome to Pong Land!")
screen.setup(width=800, height=600)
screen.bgcolor("black")

#TODO: Create and move a paddle
paddle_1 = Turtle()
paddle_1.penup()
paddle_1.goto(P1_START)
paddle_1.color("white")
paddle_1.shape("square")
paddle_1.shapesize(stretch_len=1, stretch_wid=5)



def move_up():
    y_coor = paddle_1.ycor()
    y_coor += 20
    paddle_1.goto(x=350, y=y_coor)


def move_down():
    y_coor = paddle_1.ycor()
    y_coor -= 20
    paddle_1.goto(x=350, y=y_coor)


screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.listen()

#TODO: Create another paddle
#TODO: Create the ball and make it move
#TODO: Detect collisions with wall and bounce
#TODO: Detect collision with paddle
#TODO: Detect when paddle misses
#TODO: Keep score

screen.exitonclick()
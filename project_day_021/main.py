# Day 21 Project: Pong-head

from turtle import Screen
from paddle import Paddle

R_PADDLE_START = (350, 0)
L_PADDLE_START = (-350, 0)

# Create the screen
screen = Screen()
screen.title("Welcome to Pong Land!")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle(R_PADDLE_START)
l_paddle = Paddle(L_PADDLE_START)

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


screen.listen()

game_is_on = True
while game_is_on:
    screen.update()


# TODO: Create the ball and make it move
# TODO: Detect collisions with wall and bounce
# TODO: Detect collision with paddle
# TODO: Detect when paddle misses
# TODO: Keep score

screen.exitonclick()

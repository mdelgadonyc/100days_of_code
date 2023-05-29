# Day 21 Project: Pong-head

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

R_PADDLE_START = (350, 0)
L_PADDLE_START = (-350, 0)
BALL_START = (0, 0)

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

ball = Ball(BALL_START)

# Get ball to automatically move to top right of screen as soon as game begins

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collisions with wall and bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when either right or left paddle misses
    if ball.xcor() > 380:
        ball.restart()

    if ball.xcor() < -380:
        ball.restart()

# TODO: Keep score

screen.exitonclick()

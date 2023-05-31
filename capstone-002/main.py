# Day 23 Project: [Capstone] Turtle Crossing

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle
# north.

tommy = Player()

screen.listen()
screen.onkey(tommy.move, "Up")

car_manager = CarManager()
car_manager.new_car()

# TODO: Detect when the turtle player collides with a car and stop the game if this happens.

# TODO: Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When
#  this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about
#  creating an attribute and using the MOVE_INCREMENT to increase the car speed.

# TODO: Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a
#  successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the
#  centre.

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.new_car()
    car_manager.move_cars()

    screen.update()

screen.exitonclick()

# Day 23 Project: [Capstone] Turtle Crossing

import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle
# north.

tommy = Player()

screen.listen()
screen.onkey(tommy.move, "Up")

scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.new_car()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.new_car()
    car_manager.move_cars()

    # Detect when the turtle player collides with a car and stop the game if this happens.
    for car in car_manager.cars:
        if car.distance(tommy) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When
    #  this happens, return the turtle to the starting position and increase the speed of the cars.
    if tommy.is_at_finish_line():
        tommy.reset()
        car_manager.speedup()
        scoreboard.level_up()

    screen.update()

screen.exitonclick()

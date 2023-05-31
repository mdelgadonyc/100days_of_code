from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def new_car(self):
        # Create cars that are 20px high by 40px wide that are randomly generated along the y-axis. No cars should
        # be generated in the top and bottom 50px of the screen (think of it as a safe
        #  zone for our little turtle).

        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        # Move existing cars to the left of the screen
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)


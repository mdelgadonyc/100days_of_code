from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []

    def new_car(self):
        # Create cars that are 20px high by 40px wide that are randomly generated along the y-axis. No cars should
        # be generated in the top and bottom 50px of the screen (think of it as a safe
        #  zone for our little turtle).

        car = Turtle()
        car.shape("square")
        car.setheading(180)
        color = random.choice(COLORS)
        y_cor = random.randint(-250, 250)
        car.color(color)
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(300, y_cor)
        self.cars.append(car)

    def move_cars(self):
        # Move existing cars to the left of the screen
        for car in self.cars:
            cor_x = car.xcor()
            cor_x -= STARTING_MOVE_DISTANCE
            car.goto(cor_x, car.ycor())

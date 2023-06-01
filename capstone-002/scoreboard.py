from turtle import Turtle

LOCATION_LEVEL_TEXT = (-280, 260)
FONT = ("Courier", 20, "normal")


# TODO: Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a
#  successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the
#  centre.

class Scoreboard(Turtle):
    level = 1

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(LOCATION_LEVEL_TEXT)
        self.hideturtle()
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
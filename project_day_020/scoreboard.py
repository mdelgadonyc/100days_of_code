from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(-10, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:  {self.score}", move=False, font=('Arial', 15, 'normal'), align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(-10, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, font=FONT, align=ALIGNMENT)

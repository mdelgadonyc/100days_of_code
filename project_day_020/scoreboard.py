from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # TODO: Obtain initial self.high_score from the saved file data.txt
        self.file = open("data.txt", "r+")
        self.high_score = int(self.file.read())
        print(f"current high_score is: {self.high_score}")
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
            # TODO: Overwrite current high score in file data.txt with the new high score.
            self.file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, font=FONT, align=ALIGNMENT)

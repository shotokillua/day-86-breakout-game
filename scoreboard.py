from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Veradana", 12, "bold")

with open("highscore.txt") as file:
    contents = file.read()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(contents)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=-200, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as high_score:
                high_score.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

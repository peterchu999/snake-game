from turtle import Turtle
from score_file_manager import save_high_score, get_high_score
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.refresh_score()
        self.hideturtle()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            save_high_score(self.high_score)
        self.score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

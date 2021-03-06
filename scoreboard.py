from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
        self.goto(0,-50)
        self.write(f"Your score is {self.score}", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 10, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gain_points(self):
        self.clear()
        self.score += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

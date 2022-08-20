from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 10, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}", align=ALIGNMENT, font=FONT)

    def gain_points(self):
        self.score += 1
        self.update_score_board()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score_board()

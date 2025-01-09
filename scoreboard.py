from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier',50,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("GREEN")
        self.speed("fastest")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_board()



    def update_board(self):
        self.goto(-100, 230)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 230)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)



    def update_lscore(self):
        self.l_score += 1
        self.clear()
        self.update_board()

    def update_rscore(self):
        self.r_score += 1
        self.clear()
        self.update_board()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)



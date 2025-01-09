from turtle import Turtle
DISTANCE = 20
class Paddle(Turtle):
    def __init__(self,pxy):
        super().__init__()
        self.color('MAROON')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1) # 100,20
        self.speed("fastest")
        self.pu()
        self.goto(pxy)

    def up(self):
        new_y = self.ycor() + DISTANCE
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - DISTANCE
        self.goto(self.xcor(), new_y)







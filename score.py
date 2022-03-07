from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def count(self,num):
        self.clear()
        self.color("white")
        self.goto(0,260)
        self.write("SCORE :"+str(num),True,align="center",font=("Courier",30,"normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",True,align="center",font=("Courier",30,"normal"))


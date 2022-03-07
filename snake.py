from turtle import Turtle
POS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.lis_tur=[]
        self.heading = 'right'
        self.snakeCreation()
        self.head = self.lis_tur[0]

    def snakeCreation(self):
        for i in POS:
            self.add_tail(i)

            # self.lis_tur.append(Turtle())
            # self.lis_tur[i].penup()
            # self.lis_tur[i].color("white")
            # self.lis_tur[i].shape("square")
            # self.lis_tur[i].goto(x=-(i*20),y=0)

    def add_tail(self,position):
        new_tail = Turtle("square")
        new_tail.penup()
        new_tail.color("white")
        new_tail.goto(position)
        self.lis_tur.append(new_tail)


    def extend(self):

        self.add_tail(self.lis_tur[-1].position())
        # self.lis_tur.append(Turtle())
        # self.lis_tur[-1].penup()
        # self.lis_tur[-1].color("white")
        # self.lis_tur[-1].shape("square")

        # c = Turtle()
        # c.color("white")
        # c.penup()
        # c.shape("square")
        # self.lis_tur.append(c)


    def move(self):
        for i in range(len(self.lis_tur)-1,0,-1):
            x = self.lis_tur[i-1].xcor()
            y = self.lis_tur[i-1].ycor()
            self.lis_tur[i].goto(x,y)

        self.lis_tur[0].forward(20)

    def up(self):
        if self.heading=='up' or self.heading=='down':
            pass
        else:
            self.lis_tur[0].setheading(90)
            self.heading = 'up'

    def down(self):
        if self.heading=='down' or self.heading=='up':
            pass
        else:
            self.lis_tur[0].setheading(270)
            self.heading = 'down'

    def right(self):
        if self.heading=='right' or self.heading=='left':
            pass
        else:
            self.lis_tur[0].setheading(0)
            self.heading = 'right'

    def left(self):
        if self.heading=='left' or self.heading=='right':
            pass
        else:
            self.lis_tur[0].setheading(180)
            self.heading = 'left'

    def position(self):
        return (self.lis_tur[0].xcor(),self.lis_tur[0].xcor())
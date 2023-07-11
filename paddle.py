from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.goto(x=0, y=-290)


    def move_right(self):
        new_x = self.xcor() + 40
        self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        new_x = self.xcor() - 40
        self.goto(x=new_x, y=self.ycor())




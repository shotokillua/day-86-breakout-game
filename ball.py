from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=-268)
        self.x_move = 1
        self.y_move = 1


    def vert_bounce(self):
        self.y_move *= -1

    def horiz_bounce(self):
        self.x_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def new_ball(self):
        self.goto(x=0, y=-268)
        self.vert_bounce()


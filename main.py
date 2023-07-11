# Import necessary libraries
from turtle import Turtle

# create ball object from Turtle class
# create paddle object from Turtle class
# create scoreboard from Turtle class
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(n=0) # allows for continuous animation (n=0 means wait for 0 screen updates before refreshing page)

# create paddle and ball and scoreboard
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

# create the bricks
bricks = []
brick_colors = ['red', 'orange', 'yellow', 'green', 'blue']

# loop to create the bricks
for row in range(5):  # 5 is number of brick rows
    for column in range(-4, 4):  # 8 is number of brick columns
        # calculate the position of each brick
        x = (column * 150) / 2 + 30  # 75 is the horizontal length of each brick
        y = 200 - row * 25  # brick rows will start at y = 200 and will go down 50 pixels per row

        # Create the brick
        brick = Turtle()
        brick.shape("square")
        brick.color(brick_colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=3.5)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

game_on = True
while game_on:

    screen.update()
    ball.move()

    # detect wall collision
    if ball.xcor() > 285 or ball.xcor() < -290:
        ball.horiz_bounce()

    if ball.ycor() > 290:
        ball.vert_bounce()

    # detect for paddle collision
    if ball.distance(paddle) < 60 and ball.ycor() < -268:  # remember this distance is from the center of the rectangle turtle, not the edge of the turtle
        ball.vert_bounce()

    for brick in bricks:
        # if ball.distance(brick) < 40 and ball.x_move == 0.75 or ball.x_move == -0.75: # The ball.x_move conditions were for the scenario where the bricks
                                                                                        # are large enough to be hit from the L/R side rather than just from the bottom
                                                                                        # thus the horiz_bounce() call below, but in this game it's not needed,
                                                                                        # you may not even need the ball.x_move conditions as you didn't need the
                                                                                        # ball.y_move conditions for the vert bounce case
        #     ball.horiz_bounce()
        #     # brick.goto(1000, 1000)  # Move the brick out of the screen
        #     bricks.remove(brick)  # Remove the brick from the list
        if ball.distance(brick) < 40:
            ball.vert_bounce()
            brick.goto(1000, 1000) # Move the brick out of the screen
            bricks.remove(brick) # Remove the brick from the list

            scoreboard.increase_score()
            scoreboard.update_scoreboard()

    # game over condition
    if ball.ycor() < -290:
        game_on = False

        # display game over message and exit the game
        message = Turtle()
        message.color("white")
        message.penup()
        message.goto(x=0, y=0)
        message.write(f"Game over. Your score is: {40 -len(bricks)}.", align="center", font=("Verdana", 24, "bold"))

        scoreboard.reset()

    elif len(bricks) == 0:
        game_on = False

        message = Turtle()
        message.color("white")
        message.penup()
        message.goto(x=0, y=0)
        message.write("Winner! Your score is: 40.", align="center", font=("Verdana", 24, "bold"))

        scoreboard.reset()

screen.mainloop()


from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from blocks import Block
from score import Scoreboard
import time


# screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Atari Breakout")
screen.tracer(0)

# paddle
down_paddle = Paddle((0, -250))
screen.listen()
screen.onkey(down_paddle.go_left, "Left")
screen.onkey(down_paddle.go_right, "Right")

# ball
ball = Ball()

# blocks
blocks = Block()
blocks.create_boxes()

# score
scoreboard = Scoreboard()

failures = 0
game_on = True
while game_on:

    time.sleep(ball.sleep)
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bouncey()

    if ball.ycor() < -340:
        failures += 1
        ball.reset_position()
        if failures == 5:
            game_on = False
            scoreboard.game_over()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bouncex()

    # ball bounce from paddle
    if ball.distance(down_paddle) < 70 and ball.ycor() < -220:
        ball.bouncey()

#     detect collision with a box
    for box in blocks.all_boxes:
        if ball.distance(box) < 50:
            box.hideturtle()
            box.goto(1000, 1000)
            ball.bouncey()
            scoreboard.increase_score(box.color)
            # print(box.color)


screen.exitonclick()

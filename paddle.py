from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shapesize(1, 7)
        self.penup()
        self.shape("square")
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 25
        # self.goto(self.ycor(), new_x)
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 25
        # self.goto(self.ycor(), new_x)
        self.goto(new_x, self.ycor())

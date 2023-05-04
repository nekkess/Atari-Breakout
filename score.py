from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-320, -270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 16, "normal"))

    def increase_score(self, color):
        if color()[0] == 'blue':
            self.score += 1
        elif color()[0] == 'green':
            self.score += 3
        elif color()[0] == 'yellow':
            self.score += 5
        elif color()[0] == 'red':
            self.score += 10
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 36, "normal"))

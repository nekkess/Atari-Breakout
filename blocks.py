from turtle import Turtle

COLORS = ["blue", "green", "yellow", "red"]


class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.all_boxes = []

    def create_boxes(self):
        y_pos = 30
        for line in range(0, 4):
            x_pos = 347
            for box in range(0, 8):
                new_box = Turtle('square')
                new_box.shapesize(3, 4)
                new_box.penup()
                # new_box.color(random.choice(COLORS))
                new_box.color(COLORS[line])
                new_box.goto((x_pos, y_pos))
                x_pos -= 100
                self.all_boxes.append(new_box)
            y_pos += 80

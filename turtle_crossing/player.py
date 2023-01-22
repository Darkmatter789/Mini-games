from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.reset()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.seth(90)
        self.goto(STARTING_POSITION)

    def go_faster(self):
        pass
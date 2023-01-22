from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.seth(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x_pos, y_pos)

    def up(self):
        if self.ycor() < 350:
            self.forward(80)

    def down(self):
        if self.ycor() > -350:
            self.backward(80)

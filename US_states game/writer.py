from turtle import Turtle

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.ht()


    def write_correct_state(self, state, x, y):
        self.goto(x,y)
        self.write(state, align="center", font=('Arial', 7, 'normal'))
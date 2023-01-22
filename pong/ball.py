from turtle import Turtle
import random

DISTANCE = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
     
    def bounce(self):
        self.y_move *= -1
    
    def paddled(self):
        self.x_move *= -1
        self.move_speed *= 0.5

    def reset(self):
        self.move_speed = 0.05
        self.home()
        self.x_move *= -1
        
   
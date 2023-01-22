from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.y_pos = random.randint(-230, 250)
        self.x_pos = random.randint(300, 800)
        self.reset()
    
    def move(self):
        self.backward(self.move_speed)
        
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def reset(self):
        self.goto(self.x_pos, self.y_pos)

from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()
        self.goto(-200, 250)
        self.level = 0

    def update_level(self):
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def end_game(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.update_level()

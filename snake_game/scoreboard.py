from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.ht()
        self.score = 0
        self.highscore = 0
        self.load_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def load_high_score(self):
        with open("snake_game/HS_data.txt", mode="r") as f:
            contents = int(f.read())
        self.highscore = contents

    def update_high_score(self):
        with open("snake_game/HS_data.txt", mode="w") as f:
            num_to_str = str(self.highscore)
            f.write(num_to_str)


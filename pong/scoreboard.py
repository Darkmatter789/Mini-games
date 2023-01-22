from turtle import Turtle

ALIGNMENT = 'center'
SCORE_FONT = ('Arial', 50, 'normal')
FONT = ('Arial', 12, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.goto(x, y)
        self.score = 0

    def update_scoreboard(self):
        self.write(f'{self.score}', align=ALIGNMENT, font=SCORE_FONT)

    def end_game(self, winner):
        self.goto(0,0)
        self.write(f'GAME OVER\n    {winner} wins!', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
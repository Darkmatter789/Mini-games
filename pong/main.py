from scoreboard import ScoreBoard
from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

left_score = ScoreBoard(-50, 320)
right_score = ScoreBoard(50, 320)

ball = Ball()
l = Paddle(-550, 0)
r = Paddle(550, 0)

for num in range(-400 , 400, 40):
    t = Turtle()
    t.color('white')
    t.shape('square')
    t.shapesize(stretch_wid=.8, stretch_len=.2)
    t.penup()
    t.goto(0, num)

screen.listen()
screen.onkeypress(r.up, "Up")
screen.onkeypress(r.down, "Down")
screen.onkeypress(l.up, "w")
screen.onkeypress(l.down, "s")


running = True
while running:
    time.sleep(ball.move_speed)
    screen.update()
    left_score.update_scoreboard()
    right_score.update_scoreboard()
    ball.move()
    
    if ball.ycor() > 379:
        ball.bounce()
    elif ball.ycor() < -370:
        ball.bounce()
    
    if ball.distance(r) < 50 and ball.xcor() > 520:
        ball.paddled()
    elif ball.distance(l) < 50 and ball.xcor() < -520:
        ball.paddled()
       
    if ball.xcor() > 580:
        left_score.update_score()
        ball.reset()
        time.sleep(0.3)

    if ball.xcor() < -580:
        right_score.update_score()
        ball.reset()
        time.sleep(0.3)
    
    if right_score.score == 10 and right_score.score > left_score.score:
        running = False
        right_score.end_game('Right')
    elif left_score.score == 10 and left_score.score > right_score.score:
        running = False
        left_score.end_game('Left')

screen.exitonclick()
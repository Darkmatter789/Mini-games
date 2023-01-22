import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
cars = [CarManager() for _ in range(20)]
level = Scoreboard()

screen.listen()
screen.onkeypress(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    level.update_level()

    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.reset()
        elif tim.distance(car) < 20:
            level.end_game()
            game_is_on = False    
    if tim.ycor() > 280:
        for car in cars:
            car.increase_speed()
        tim.reset()
        level.next_level()

    if tim.distance(car) < 20:
        level.end_game()
        game_is_on = False

       
    
screen.exitonclick()
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turt = Player()
score= Score()

screen.onkeypress(turt.move_fwd, "Up")
screen.onkeypress(turt.move_bwd, "Down")
car1= CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car1.create_cars()
    car1.move()
    if turt.ycor() in [-100,50,180]:
        car1.increase_speed()
    if turt.ycor() == 280:
        score.win_game()
        time.sleep(1)
        game_is_on= False
    for car in car1.all_cars:
        if car.distance(turt) < 18:
            score.game_over()
            time.sleep(1)
            game_is_on = False

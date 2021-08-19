import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars=[]


    def create_cars(self):
        chance = random.randint(1,6)
        if chance == 6:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.y_cor = random.randint(-220,280)
            new_car.x_cor = 290
            new_car.goto(new_car.x_cor,new_car.y_cor)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)

    def getposition(self):
        for cars in self.all_cars:
            x_cor=cars.xcor()
            y_cor=cars.ycor()
            pos = (x_cor, y_cor)
            return pos

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += 5


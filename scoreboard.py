FONT = ("Calibre", 10, "normal")
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.write("You are struck by car!! GAME OVER", align= "center", font=FONT)

    def win_game(self):
        self.write("You reached the end without harm!! YOU WON", align= "center", font=FONT)


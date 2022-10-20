import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        self.goto((random.randrange(-280,280)),(random.randrange(-280,250)))
        self.refresh()

    def refresh(self):
        self.goto((random.randrange(-280,280)),(random.randrange(-280,250)))
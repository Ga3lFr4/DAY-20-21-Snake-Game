import turtle
from turtle import Turtle
import random

food_shape = turtle.textinput("Food shape", "Please chose what food you want to eat (circle, turtle, square)")
food_color = turtle.textinput("Food color", "Please chose food color (white/green/blue/purple)")
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(food_shape)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(food_color)
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
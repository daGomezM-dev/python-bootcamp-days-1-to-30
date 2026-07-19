from turtle import Turtle, colormode, Screen
from random import randint

CIRCUNFERENCE = 360 

timmy = Turtle()
colormode(255)

for i in range(3,11):
    degrees = CIRCUNFERENCE / i
    timmy.pencolor((randint(0,255), randint(0,255), randint(0,255)))
    for j in range (0, i):
        timmy.forward(50)
        timmy.right(degrees)


screen = Screen()
screen.exitonclick()
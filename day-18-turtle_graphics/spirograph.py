import turtle as t
import random as r

timmy = t.Turtle()
timmy.pensize(5)
t.colormode(255)
timmy.speed(0)

directions = [0,90,180,270]

for i in range (0, 100):
    timmy.color(r.randint(0,255), r.randint(0,255), r.randint(0,255))
    timmy.circle(100)
    timmy.left(3.6)
        

screen = t.Screen()
screen.exitonclick()
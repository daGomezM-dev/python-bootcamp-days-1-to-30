import turtle as t
import random as r

timmy = t.Turtle()
timmy.pensize(10)
t.colormode(255)

directions = [0,90,180,270]

for i in range (0, 100):
    timmy.color(r.randint(0,255), r.randint(0,255), r.randint(0,255))
    timmy.forward(30)
    timmy.setheading(r.choice(directions))
        

screen = t.Screen()
screen.exitonclick()

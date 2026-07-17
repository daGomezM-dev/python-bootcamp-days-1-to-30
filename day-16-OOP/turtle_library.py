"""
import turtle
timmy = turtle.Turtle()
"""

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("IndianRed1")
timmy.forward(100)

my_screen = Screen()

# To access to an attribute of the object, we use .
print(my_screen.canvheight) # access to attribute
my_screen.exitonclick()
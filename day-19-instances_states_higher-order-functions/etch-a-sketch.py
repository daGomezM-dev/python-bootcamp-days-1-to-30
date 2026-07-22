from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def turn_right():
    tim.right(20)

def turn_left():
    tim.left(20)

def clear():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun= move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
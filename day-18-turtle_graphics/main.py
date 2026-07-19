# First of all I install the package colorgram.py (which allow us to extract the RGB values of an image)

import colorgram
import turtle as t
import random as ra

colors = colorgram.extract('python-bootcamp-days-1-to-30/day-18-turtle_graphics/hirst.png', 10) # Colors list
t.colormode(255)

rgb_color_list = []

for color in colors:
    r = color.rgb.r #rgb is a namedtuple, so we can access to the elements by typing . 'name'
    g = color.rgb.g
    b = color.rgb.b
    tuple = (r, g, b)
    rgb_color_list.append(tuple)

print(rgb_color_list)

# paint 10 x 10 rows of spots 
# Dots: 20 size, 50 space between them

# dos for

tim = t.Turtle()

tim.penup()
tim.goto(-220, -220)
pos_x = tim.xcor() # Obtengo la coordenada x inicial de tim
pos_y = tim.ycor() # Obtengo la coordenada y inicial de tim

for row in range(0,10):
    for col in range(0,10):
        # dibujamos esfera de 20
        # movemos 50 de espacio (sin puntar)
        tim.pendown()
        tim.pencolor(ra.choice(rgb_color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    tim.goto(pos_x, pos_y + ((row+1) * 50))

tim.penup()
tim.goto(pos_x, pos_y)

screen = t.Screen()
screen.exitonclick()
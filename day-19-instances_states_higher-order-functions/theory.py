from turtle import Turtle, Screen
"""Recordatorio
    # Una función puede almacenarse en una variable:
    def add(n1, n2)
        return n1+n2

    fun = add

    fun() # es como si hicieramos add()
"""

# En este ejemplo, calculator es una higher order function
def add(n1,n2):
	return n1+n2
	
def substract(n1,n2):
	return n1-n2
	
def multiply(n1,n2):
	return n1*n2
	
def calculator(n1, n2, func):
	return func(n1,n2)


# Listeners:
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards()) # Esta notacion de argumentos esla KEYWORD ARGUMENTS, la que usaba antes era la POSITIONAL ARGUMENTS
# Cuando usamos una funcion que no hemos implementado nosotros es recomendable utilizar la KEYWORD ARGUMENTS
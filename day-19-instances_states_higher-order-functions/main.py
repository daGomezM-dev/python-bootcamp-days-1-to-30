from turtle import Turtle, Screen
import random as ra


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


up = 0
turtles = {}
random_advance = [0, 5, 10, 15]

for color in colors:
    newTurtle = Turtle("turtle")
    newTurtle.color(color)
    newTurtle.penup()
    newTurtle.goto(x=-230, y=-100 + up)

    turtles[color] = newTurtle # añado la tortuga al dictionary, con la key que es su color
    up += 30

# van a ir dando pasos aleatorios hacia delante (0, 10, 20, 30)

def start_race(turtles):
    while True: 
        for key in turtles:
            turtles[key].forward(ra.choice(random_advance))
            if turtles[key].xcor() >= 250:
                return turtles[key]

def check_users_bet(user_bet, turtle_winner):
    print(f"The " + str(turtle_winner.pencolor()) + " turtle was the winner!")
    if user_bet.lower() == turtle_winner.pencolor():
        print("Congrats! You've won the bet")
    else:
        print(f"Sorry, the {user_bet} turtle has lose")

def main():
    winner = start_race(turtles)
    check_users_bet(user_bet, winner)

if __name__ == "__main__":
    main()



screen.exitonclick()
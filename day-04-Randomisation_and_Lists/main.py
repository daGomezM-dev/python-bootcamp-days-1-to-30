"""
You are going to build a Rock, Paper, Scissors game.
You will need to use what you have learnt about randomisation and Lists to achieve this
"""
import random

# Solution:

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# User choice
selected = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if selected < 0 or selected > 2:
    selected = input("Select an option in the range of 0 to 2. ")
else:
    if selected == 0:
        print(rock)
    elif selected == 1:
        print(paper)
    else:
        print(scissors)

# Random parameter
random_num = random.randint(0,2)
print("Computer choose: ")
if random_num == 0: # I could use a function, for example: printChoice, which based on the argument, print the correct ascii art
    print(rock)
elif random_num == 1:
    print(paper)
else:
    print(scissors)

# Final result (logic)
if selected == 0:
    if random_num == 0:
        print("It's a draw!")
    elif random_num == 1:
        print("You loose")
    else:
        print("You win")
elif selected == 1:
    if random_num == 0:
        print("You win")
    elif random_num == 1:
        print("It's a draw!")
    else:
        print("You loose")
else:
    if random_num == 0:
        print("You loose")
    elif random_num == 1:
        print("You win")
    else:
        print("It's a draw!")
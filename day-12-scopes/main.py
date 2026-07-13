# The goal is to build a guess the number game.
# It will offer to the user two game modes: easy or hard
# Easy mode: 10 attemps
# Hard mode: 5 attemps 
# After each attemp, the programm will give hints to the user (Too high, Too low)
import random

EASY_ATTEMPS = 10
HARD_ATTEMPS = 5

def intro():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    return input("Choose a dificulty. Type 'easy' or 'hard': ")

def main():
    num = random.randint(1, 100)
    mode = {"easy": EASY_ATTEMPS, "hard": HARD_ATTEMPS}
    attemps = mode[intro()]
    win = False
    while attemps > 0 and not win:
        print(f"You have {attemps} attemps remaining to guess the number. ")
        guess = int(input("Make a guess "))
        if guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        else:
            print(f"You got it! the answer was {num}")
            win = True

        attemps -= 1
    if attemps == 0 and not win:
        print(f"You have run out of guesses, the answer was {num}")

if __name__ == "__main__":
    main()

"""

I have to do a hangman game. The course offers me steps and todo's in order to guide me, however, 
I will try to do it by my own.

"""

import random

# I create three different wordlists. The words are in spanish (my native language)
wordlist_car = ["volante", "chasis", "carroceria", "llanta", "aleron", "parabrisas"]
wordlist_food = ["spaghetti", "pizza", "ensalada", "hamburguesa", "dimsum", "yakisoba", "arroz", "melon", "mango"]
wordlist_countries = ["polonia", "africa", "españa", "italia", "francia", "ghana", "austria", "pekin", "vietnam"]

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def randomWord():
    """
    Randomly chooses a word from one of the available word lists

    Returns: 
        str: The word chosen
    """
    list_topic = random.randint(0,2)
    if list_topic == 0:
        w = wordlist_car[random.randint(0, len(wordlist_car) -1)]
    elif list_topic == 1:
        w = wordlist_food[random.randint(0, len(wordlist_food) -1)]
    else:
        w = wordlist_countries[random.randint(0, len(wordlist_countries) -1)]

    return w

def fillWordProgress(word_length, blank_word):
    """
    It fills the blank word with "_"

    Args:
        word_length (int): the lenght of the word to guess
        blank_word (list): the list that is going to be filled with "_"

    Returns:
        blank_word (list): the word in format "___" to guess 
    """

    for n in range(0, word_length):
        blank_word.append("_")

    return blank_word

def letterAdvance(letter_choice, wordToGuess, word_progress, remainingLives):
    if wordToGuess.count(letter_choice) > 0:
        for i in range (0, len(wordToGuess)):
            if wordToGuess[i] == letter_choice:
                word_progress[i] = letter_choice
        print("".join(word_progress))
    else: 
        print(f"You guessed {letter_choice}, that's not in the word. You lose a life ")
        remainingLives = remainingLives-1
    return remainingLives

def main():
    win = False
    remainingLives = 6
    word_progress = []
    wordToGuess = randomWord()
    word_progress = fillWordProgress(len(wordToGuess), word_progress)

    # main loop of the program
    while remainingLives > 0:
        print("Word to guess: " + "".join(word_progress))
        letter = input("Guess a letter: ")
        remainingLives = letterAdvance(letter, wordToGuess, word_progress, remainingLives)
        print(stages[remainingLives])
        if "_" not in word_progress: 
            print("You win!")
            break
        print(f"****************************{remainingLives}/6 LIVES LEFT****************************")

    if remainingLives == 0:
        print(f"***********************IT WAS " + "".join(wordToGuess) + "! YOU LOSE**********************")

if __name__ == "__main__":
    main()


"""
if __name__ == "__main__":
    main()

Explanation: Each program has it's special variable __name__ . 
The __name__ variable in the program which is being run has the value "__main__"
Lets say that our program has imported calculator (a module calculator.py that i've created previously)
and I just want to have access to my calculator's module functions, but not to run the calculator.py as the main program.
In that case, when the program run the module calculator and get to the if clause, the __name__ variable is not
going to be "__main__", is going to be "__calculator__" so the main function in the calculator module is not going to 
be executed. However, when the compiler executes the if __name__ == "__main__" clause in our main program, the
main() function is going to be executed
"""


"""
Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""
import random

# The ace count as 11 if the sum of the previous cards plus 11 don't overpass 21, 
# in other case, it will count as 1

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# 2 cards delivered to the player 
# 2 cards delivered to the computer (one concealed, the other visible)

# The computer just play with 2 cards

def randomCard():
    """ It returns a random card from the deck """
    pos = random.randint(0, len(cards)-1)
    return cards[pos]

def createInitialCards():
    """ It returns a list with the initial pair of cards """
    card1 = randomCard()
    card2 = randomCard()
    return [card1, card2]

def addNewRandomCard(l_cards):
    """ Adds a new card to the list """
    l_cards.append(randomCard())

def printState(u_cards, c_cards):
    print(f"Your cards: {u_cards}, current score: {sum(u_cards)}")
    print(f"Computer's first card: {c_cards[0]}")  

def dealerBehaviour_1(c_cards, user_score):
    while sum(c_cards) < user_score:
        addNewRandomCard(c_cards)

def dealerBehaviour_2(c_cards):
    random_limit = random.randint(14,18)

    while sum(c_cards) <= random_limit: # 16 or higher the dealer will stand
        addNewRandomCard(c_cards)

def computerProgress(c_cards, user_score):
    """ Simulate the dealer participation """

    random_number = random.randint(1,2)
    if random_number == 1:
        dealerBehaviour_1(c_cards, user_score)
    elif random_number == 2:
        dealerBehaviour_2(c_cards)
    
def printOverpassLoose(u_cards, c_cards):
    print(f"Your final hand: {u_cards}, final score: {sum(u_cards)}")
    print(f"Computer's final hand: [{c_cards[0]}], final score: {c_cards[0]}")
    print("You went over, you loose ;( ")

def printLoose(u_cards, c_cards):
    print(f"Your final hand: {u_cards}, final score: {sum(u_cards)}")
    print(f"Computer's final hand: {c_cards}, final score: {sum(c_cards)}")
    print("You loose ;( ")

def printWin(u_cards, c_cards):
    print(f"Your final hand: {u_cards}, final score: {sum(u_cards)}")
    print(f"Computer's final hand: {c_cards}, final score: {sum(c_cards)}")
    print("You win!!")

def game():
    contin = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
    while contin == 'y':
        print("\n" * 100)
        user_cards = createInitialCards()
        computer_cards = createInitialCards()
        printState(user_cards, computer_cards)
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        print("\n")  

        while hit == 'y':
            addNewRandomCard(user_cards)
            printState(user_cards, computer_cards)
            if sum(user_cards) > 21: # user loses  
                printOverpassLoose(user_cards, computer_cards)
                break
            elif sum(user_cards) == 21: # time to check if computer do 21
                computerProgress(computer_cards, sum(user_cards))
                if sum(computer_cards) == 21:
                    printLoose(user_cards, computer_cards)
                    break
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if sum(user_cards) <= 21:
            computerProgress(computer_cards, sum(user_cards))
            if sum(computer_cards) <= 21:
                if sum(computer_cards) >= sum(user_cards):
                    printLoose(user_cards, computer_cards)
                    
                else: 
                    printWin(user_cards, computer_cards)       
                    
            else:
               printWin(user_cards, computer_cards)
                
        contin = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")

game()
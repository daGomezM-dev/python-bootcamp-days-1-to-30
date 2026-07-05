"""

Functionality
Each person writes their name and bid.
The program asks if there are others who need to bid. 
If so, then the computer clears the output (prints several blank lines) 
then loops back to asking name and bid.
Each person's name and bid are saved to a dictionary.
Once all participants have placed their bid, the program works out who has the
highest bid and prints it.
"""

def newParticipant(dictionary):
    name = input("What's your name? ")
    bid = int(input("What's your bid? ")) # ALWAYS RETURN A STR, be careful
    dictionary[name] = bid

# It returns a dictionary (that could be just a tuple) composed by the name and the bid of the winner
def auctionWinner(dictionary):
    winnerBid = 0
    winnerName = ""
    for key in dictionary:
        if dictionary[key] > winnerBid:
            winnerBid = dictionary[key]
            winnerName = key
    return {winnerName: winnerBid}

def main():

    participants = {} # empty dictionary
    moreParticipants = True

    while moreParticipants:
        newParticipant(participants)
        more = input("There's more participants? yes/no ")
        if more == "no":
            moreParticipants = not moreParticipants

    winner = auctionWinner(participants)
    print(winner)

if __name__ == "__main__":
    main()
import game_data
import art
import random

# Data es un array de diccionarios (cada diccionario es un dato)
# coger inicialmente dos posiciones aleatorias del array (datos a comparar)


def randomData(data):
    """ 
    Select a random data from de data list 
    
    Args:
        data (list): the list of dictionaries (each one is a data piece to compare)

    Returns:
        selectedData (dictionary): data piece to compare
    """
    num = random.randint(0, len(data)-1)
    return data[num]

def printData(d_data):
    """
    It prints the piece of data (dictionary) based on the format required

    Args:
        d_data (dictionary): piece of data from the data list 
    """
    return f"{d_data['name']}, a {d_data['description']}, from {d_data['country']}"

def higher (d1, d2):
    """
    It compares both datas, the currentData is always the correct answer

    Args: 
        d1 (dictionary): data 1
        d2 (dictionary): data 2
    
    Returns:
        d1 (dictionary): data 1
        d2 (dictionary): data 2
    """

    # I'm assuming that there's no data with the exact same number of followers
    if d1["follower_count"] > d2["follower_count"]:
        return d1
    else:
        return d2

def checkUserInput(correct_option, u_input):
    """
    It checks if the user has choosen the correct option

    Args:
        correct_option (dictionary): correct data
        u_input (dictionary): user choice
    """
    return correct_option == u_input


# Inicialmente dos randomData a comparar
# Bucle while: mientras correct, continua
# currentData: variable que guarde la data a comparar en la siguiente vuelta del bucle si acierto
# crear un diccionario A, B y los datas


def main():
    print(art.logo)
    correct = True
    counter = 0 # contador de aciertos
    options = {"A": {}, "B": {}} # diccionario de opciones A y B
    while correct:
        if counter == 0:
            d1 = randomData(game_data.data)
            d2 = randomData(game_data.data)
            options["A"] = d1
            options["B"] = d2
            print("Compare A: " + printData(d1))
            print(art.vs)
            print("Against B: " + printData(d2))
            answer = options[input("Who has more followers? Type 'A' or 'B': ")]
            correct = checkUserInput(higher(d1, d2), answer)
            if correct == True:
                options["A"] = higher(d1, d2) # ya establezco options A como la buena para la siguiente
                counter += 1

        else:
            print(f"You're right! Current score: {counter}")
            options["B"] = randomData(game_data.data)
            print("Compare A: " + printData(options["A"]))
            print(art.vs)
            print("Against B: " + printData(options["B"]))
            answer = options[input("Who has more followers? Type 'A' or 'B': ")]
            higher_data = higher(options["A"], options["B"])
            correct = checkUserInput(higher_data, answer)
            if correct == True:
                options["A"] = higher_data # ya establezco options A como la buena para la siguiente
                counter += 1
    print(f"Sorry, that's wrong. Final score: {counter}")        

if __name__ == "__main__":
    main()
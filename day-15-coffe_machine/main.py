"""
Create a coffee machine
"""

# dictionary for all the promts available (espresso, latte, capuccino, off, report)

# dictionary for the kinds of coins 

# dictionary for the resources 

import sys # TIP: I import sys library to use the exit() function, which terminates the scrip (I will use it when the user types 'off')

# ----- Sources given -------------------------------------------------------------------------------------------------------------------

MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}

# ----- Promts functions -------------------------------------------------------------------------------------------------------------------

def report(resources, money): # Por pulir
    for key in resources:
        if key == "Coffee":
            print(f"{key}: {resources[key]}g")
        else:
            print(f"{key}: {resources[key]}ml")
    print(f"Money: ${money}")

def off():
    sys.exit()

# ----- User interaction functions -------------------------------------------------------------------------------------------------------------------

def printOptions():
    return input("What would you like? (espresso/latte/cappuccino): ")

# ----- Resources functions -------------------------------------------------------------------------------------------------------------------

def checkResourcesSufficient(user_choice):
    """ 
    Check if it can make the coffee selected with the available resources 
    
    Args:
        user_choice (dictionary): dictionary of the coffee selected by the user (contains the info related to the coffee)
        resources (dictionary): resources available in the coffee machine

    Returns:
        missing (dictionary): contains "resource" (the resource missing) and "sufficient" (boolean that warn if resource is missing or not)
    """

    missing = {"resource": "", "sufficient": True}
    for key in user_choice["ingredients"]:
        if resources[key] - user_choice["ingredients"][key] < 0:
            missing["resource"] = key
            missing["sufficient"] = False
            return missing


    return missing 

def printMissingResource(res):
    print(f"sorry, there's not enough {res}")

def substractResources(coffee_selected):
    for key in coffee_selected["ingredients"]:
        resources[key] -= coffee_selected["ingredients"][key]

# ----- Money functions -------------------------------------------------------------------------------------------------------------------

def printCoffeePrice(coffee_selected):
    print(f"Cost: {coffee_selected['cost']}")

# creamos diccionario
def collectMoney():
    """
    Ask the user for coins (quarters, dimes, nickles, pennies), and then calculate the total
    ammount of money

    Returns:
        total (float): total ammount of money introduced by the user
    """

    coins = {
        "quarters": {
            "value": 0.25,
            "ammount": 0.0
        },
        "dimes": {
            "value": 0.10,
            "ammount": 0.0
        },
        "nickles": {
            "value": 0.05,
            "ammount": 0.0
        },
        "pennies": {
            "value": 0.01,
            "ammount": 0.0
        }
    }

    total = 0
    for key in coins:
        # User input
        u_coin_introduced = float(input(f"how many {key}?: "))
        coins[key]["ammount"] = u_coin_introduced
        # Total money calculus
        total += coins[key]["value"] * coins[key]["ammount"]

    return total

def checkMoneySufficient(user_money, coffe_price):
    """
    Check if the money introduced by the user is enough to pay for the coffee selected

    Args:
        user_money (double): money introduced by the user
        coffee_price (double): coffee price
    Returns:
        sufficient (dictionary): contains the keys enough (boolean) and refund (float)
    """

    sufficient = {"enough": True, "refund": 0.0}
    refund = user_money - coffe_price
    if  refund < 0:
        sufficient["enough"] = False
        return sufficient
    else:
        sufficient["refund"] = refund
        return sufficient
        





# ----- Main -------------------------------------------------------------------------------------------------------------------

def main():
    money = 0 
    enough_money = True

    while enough_money: 
        u_choice = printOptions()
        if u_choice.lower() == "report":
            report(resources, money)
        elif u_choice.lower() == "off":
            off()
        else: 
            try:
                coffee_choice = MENU[u_choice]
            except KeyError: # Problema: si vuelve a introducir mal la opcion no la revisa
                print("You have typed an invalid coffee. Please choose an available coffee")
                u_choice = printOptions()
                coffee_choice = MENU[u_choice]

            checkRes = checkResourcesSufficient(coffee_choice)
            # Si falta algun recurso
            if not checkRes["sufficient"]:
                printMissingResource(checkRes["resource"])
            else:
                printCoffeePrice(coffee_choice)
                user_money = collectMoney()
                checkMoney = checkMoneySufficient(user_money, coffee_choice["cost"])
                if checkMoney["enough"]:
                    money += user_money - checkMoney["refund"]
                    substractResources(coffee_choice)
                    print(f"here is {round(checkMoney['refund'], 2)}$ in change")
                    print("Enjoy your " + u_choice + "!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
    return 0

if __name__ == "__main__":
    main()

# elige un cafe 
# comprobamos que tenemos los recursos para hacer dicho cafe
    # NO: sorry, there's not enough (RECURSO) VUELTA -> elige un cafe 
    # SI: please insert coins
        # how many quarters?
        # how many dimes?
        # how many nickles?
        # how many pennies?
        # CALCULOS
            # NO SUFICIENTE: Sorry that's not enough money. Money refunded. VUELTA
            # SUFICIENTE: here is (MONEY$) in change
                # here is your (COFFEE). Enjoy!
# elige un cafe
# ...


# terminamos con el dinero y termina

"""
CALCULATOR PROYECT

functionality: 
    Program asks the user to type the first number.
    Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
    Program asks the user to type the second number.
    Program works out the result based on the chosen mathematical operator.
    Program asks if the user wants to continue working with the previous result.
    If yes, program loops to use the previous result as the first number and then repeats the calculation process.
    If no, program asks the user for the fist number again and wipes all memory of previous calculations.
    Add the logo from art.py

"""


"""

TIP: store a function in a variable
    def add(n1, n2):
        return n1 + n2

    my_calculation = add # if you put () next to the name of the function, you "trigger it"

    print(my_calculation(3, 5)) # 8

"""
import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# I create a dictionary that relate keys such as "+" "-" "*" "/" with my defined functions

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }

def selectSecondAndCalculate(n1):
    op = input("+\n-\n*\n/\nPick an operation: ")
    n2 = input("What's the next number? ")
    return operations[op](n1,n2)

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
    

    
"""
The program will ask:

How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password.
Use your knowledge about Python lists and loops to complete the challenge.

-- Hard Version --
When you've completed the easy version, you're ready to tackle the hard version. 
In the advanced version of this project the final password does not follow a pattern. 
So the example above might look like this:

x$d24g*f9

And every time you generate a password, the positions of the symbols, numbers, and letters are different. 
This will make the password more difficult for hackers to crack.

The essential skill of a good programmer is using Google to find what you need. 
Your brain is for thinking, not memorising functions! You will need to Google to solve this project on the hard level. 
If you get stuck, check the hint below for what to Google.

"""
import random
import string

# Resources
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-']

# Solution (without my own functions, i haven't seen them yet)
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


# I will collect the random letters, symbols and numbers in three different lists
rand_letters = []
for l in range(1, nr_letters+1):
    # Random letter in the alphabet + add it to the letters list
    pos = random.randint(0, len(letters)-1)
    letter = letters[pos]
    rand_letters.append(letter)

rand_numbers = []
for s in range(1, nr_numbers+1):
    pos = random.randint(0, len(numbers)-1)
    number = numbers[pos]
    rand_numbers.append(number)

rand_symbols = []
for s in range(1, nr_symbols+1):
    pos = random.randint(0, len(symbols)-1)
    symbol = symbols[pos]
    rand_symbols.append(symbol)

rand_letters.extend(rand_numbers)
rand_letters.extend(rand_symbols)
simple_password = rand_letters

# Instead of googling an algorithm that randomly change the characters position of the password, I will create my own algorithm
password_lenght = len(simple_password)
iter = random.randint(0, 100) # The times that a password character change it's position
step = random.randint(1, 3) # The steps that the for loop will advance (random aswell)


for n in range(0, iter, step):
    pos_to_change = random.randint(0, password_lenght-1) # The char in pos_to_change is the one that is going to move
    final_pos = random.randint(0, password_lenght-1) # The final pos of the char that is going to move
    char_to_move = simple_password[pos_to_change] # The char we are moving
    char_moved = simple_password[final_pos] # The actual char in the final position
    # Swap
    simple_password[pos_to_change] = char_moved
    simple_password[final_pos] = char_to_move



random_password = "".join(simple_password) # It joins the elements of the list simple_password separated by ""

print("\n" + random_password + "\n")
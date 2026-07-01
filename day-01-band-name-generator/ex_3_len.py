"""
Using what you have learnt about the len() function and the input() function. Try to print out the number 
of characters in the user input. Write everything in 1 line of code 
"""

# Solution: 
print(len(input("What is your name? ")))

"""
Split each step in the previous exercise into a separate variable. One variable called username and other 
called length. Use the variable username in the len calculation.
"""

# Solution: 
username = input("What is your name? ")
length = len(username)
print(length)

"""
We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. 
Write 3 lines of code to switch the contents of the variables. 
You are not allowed to type the words "milk" or "juice". You are only allowed to use variables 
to solve this exercise.

glass1 = "milk"
glass2 = "juice"
"""

# Solution:
glass1 = "milk"
glass2 = "juice"
auxiliar = glass1 # Required to save the glass1 value
glass1 = glass2
glass2 = auxiliar
print(glass1 + " " + glass2)
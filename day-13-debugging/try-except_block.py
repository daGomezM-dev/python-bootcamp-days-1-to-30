
try: # Inside we put the part of the code that can produce the exception
    age = int(input("How old are you? "))
except ValueError: # The exception produced that we are going to manage
    print("You have typed in an invalid number. Please try again with a numerical response such as 15")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at {age}")
"""
Build a tip calculator
"""

# Solution:
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give?"))
split = float(input("How many people to split the bill?"))
total = ((bill + (bill*(tip/100)))/ split)
print(f"Each person should pay: ${round(total,2)}")

"""
Conclusion:
I have used new learned things such as the f-strings, the conversion functions and the round function
"""
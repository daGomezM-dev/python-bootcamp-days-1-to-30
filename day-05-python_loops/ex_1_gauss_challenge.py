"""
Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100
"""

# Solution:
sol = 0
for number in range(1,101):
    sol += number
print(sol)
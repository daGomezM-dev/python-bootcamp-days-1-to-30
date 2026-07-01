"""
Figure out how to pick a random name from the list of friends
"""
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Solution:
num = random.randint(0,4)
print(friends[num])
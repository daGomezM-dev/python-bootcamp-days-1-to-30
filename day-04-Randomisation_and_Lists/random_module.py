import random # Library for random numbers
import my_module # OUR module

# To create a random int
random_num = random.randint(1,10) # Generates a random int N in the range: 1 <= N <= 10
print(random_num)
print(my_module.my_favourite_number)

# To create a random float X (0 <= X < 1)
random_num_0_to_1 = random.random()
print(random_num_0_to_1)

# To create a random float X (a <= X <= b)
random_float = random.uniform(2, 10)
print(random_float)

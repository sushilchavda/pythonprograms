#Write a program to generate random numbers
#using random module.

# Program: Generate Random Numbers using random module

import random

# Generate a random integer between 1 and 100
print("Random Integer:", random.randint(1, 100))

# Generate a random floating-point number
print("Random Float:", random.random())

# Generate a random number between 10 and 50
print("Random Number:", random.uniform(10, 50))

# Select a random element from a list
numbers = [10, 20, 30, 40, 50]
print("Random Element:", random.choice(numbers))

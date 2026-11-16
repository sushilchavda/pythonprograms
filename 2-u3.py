#Write a program to demonstrate different
#import mechanisms in Python.

import math

print("Using import module:")
print("Square root:", math.sqrt(25))

from math import factorial

print("\nUsing from module import:")
print("Factorial:", factorial(5))

import math as m

print("\nUsing import module as alias:")
print("Power:", m.pow(2, 3))

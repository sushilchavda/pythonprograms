
#To write a Python program to define and use user-defined functions with different types of arguments.

def add(a, b):
    return a + b

print("Addition:", add(10, 20))

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Sushil")

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Sushil")

def total(*numbers):
    return sum(numbers)

print("Total:", total(10, 20, 30, 40))

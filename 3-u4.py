#3. Write a program to illustrate instance variables
#and class variables.

# Program to demonstrate instance variables and class variables

class Student:

    # Class variable
    college = "ABC College"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)


# Creating objects
s1 = Student("Sushil", 20)
s2 = Student("Rahul", 21)

# Displaying details
s1.display()
print()
s2.display()

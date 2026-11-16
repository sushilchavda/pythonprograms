# Program to demonstrate instance, class and static methods

class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name

    # Instance Method
    def display(self):
        print("Student Name:", self.name)

    # Class Method
    @classmethod
    def show_college(cls):
        print("College Name:", cls.college)

    # Static Method
    @staticmethod
    def message():
        print("Welcome to Python Programming")


# Creating object
s1 = Student("Sushil")

# Calling instance method
s1.display()

# Calling class method
Student.show_college()

# Calling static method
Student.message()

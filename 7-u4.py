# Program to demonstrate MRO and Magic Methods

class A:
    def show(self):
        print("Method from class A")


class B(A):
    def show(self):
        print("Method from class B")


class C(A):
    def show(self):
        print("Method from class C")


class D(B, C):
    def __init__(self, name):
        self.name = name

    # Magic method
    def __str__(self):
        return "Student Name: " + self.name


# Creating object
obj = D("Sushil")

# MRO
print("Method Resolution Order:")
print(D.mro())

# Calling method
obj.show()

# Calling magic method
print(obj)

# Program to demonstrate Single, Multilevel and Multiple Inheritance

# Single Inheritance
class Parent:
    def show_parent(self):
        print("This is Parent class")


class Child(Parent):
    def show_child(self):
        print("This is Child class")


# Multilevel Inheritance
class Grandparent:
    def show_grandparent(self):
        print("This is Grandparent class")


class Parent2(Grandparent):
    def show_parent2(self):
        print("This is Parent class")


class Child2(Parent2):
    def show_child2(self):
        print("This is Child class")


# Multiple Inheritance
class Father:
    def show_father(self):
        print("This is Father class")


class Mother:
    def show_mother(self):
        print("This is Mother class")


class Son(Father, Mother):
    def show_son(self):
        print("This is Son class")


# Single Inheritance object
print("Single Inheritance:")
obj1 = Child()
obj1.show_parent()
obj1.show_child()

# Multilevel Inheritance object
print("\nMultilevel Inheritance:")
obj2 = Child2()
obj2.show_grandparent()
obj2.show_parent2()
obj2.show_child2()

# Multiple Inheritance object
print("\nMultiple Inheritance:")
obj3 = Son()
obj3.show_father()
obj3.show_mother()
obj3.show_son()

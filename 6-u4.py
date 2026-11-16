# Program to demonstrate method overriding and polymorphism

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    # Method overriding
    def sound(self):
        print("Dog barks")


class Cat(Animal):

    # Method overriding
    def sound(self):
        print("Cat meows")


# Creating objects
dog = Dog()
cat = Cat()

# Polymorphism
dog.sound()
cat.sound()

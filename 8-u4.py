# Program to demonstrate Encapsulation and Abstraction

from abc import ABC, abstractmethod

# Abstraction
class Bank(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass


# Encapsulation
class Account(Bank):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance     # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    # Implementation of abstract method
    def calculate_interest(self):
        return self.__balance * 0.05


# Creating object
account = Account("Sushil", 10000)

# Using methods
account.deposit(2000)

print("Account Holder:", account.name)
print("Balance:", account.get_balance())
print("Interest:", account.calculate_interest())

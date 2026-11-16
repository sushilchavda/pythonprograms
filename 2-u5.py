try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("Error: cannot divide by zero")
except ValueError:
    print("Error: please enter numbers only")
else:
    print("Result =", result)
finally:
    print("Program finished")

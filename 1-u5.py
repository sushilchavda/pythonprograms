try:
    print(a)
except NameError as e:
    print("NameError      :", e)

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

try:
    print(int("abc"))
except ValueError as e:
    print("ValueError     :", e)

try:
    print("5" + 5)
except TypeError as e:
    print("TypeError      :", e)

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print("IndexError     :", e)

try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print("KeyError       :", e)

x = 10
assert x > 5
print("Assertion 1 passed")

try:
    assert x < 5, "x is not less than 5"
    print("Assertion 2 passed")
except AssertionError as e:
    print("Assertion failed:", e)

def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

print(divide(10, 2))
try:
    print(divide(10, 0))
except AssertionError as e:
    print("Error:", e)

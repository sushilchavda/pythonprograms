
print("--- List Comprehension ---")

numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]

print("Numbers:", numbers)
print("Squares:", squares)

print("\n--- Dictionary Comprehension ---")

square_dict = {x: x * x for x in numbers}

print("Square Dictionary:", square_dict)

print("\n--- Set Comprehension ---")

even_numbers = {x for x in numbers if x % 2 == 0}

print("Even Number Set:", even_numbers)

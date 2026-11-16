a = 15
b = 4


print("--- Arithmetic Operations ---")
print(f"Addition ({a} + {b})         = {a + b}")
print(f"Subtraction ({a} - {b})      = {a - b}")
print(f"Multiplication ({a} * {b})   = {a * b}")
print(f"Float Division ({a} / {b})   = {a / b}")
print(f"Floor Division ({a} // {b})  = {a // b}")
print(f"Modulus/Remainder ({a} % {b}) = {a % b}")
print(f"Exponentiation ({a} ** {b})  = {a ** b}")
print()


print("--- Relational Operations ---")
print(f"Is {a} equal to {b}? ({a} == {b})           : {a == b}")
print(f"Is {a} not equal to {b}? ({a} != {b})       : {a != b}")
print(f"Is {a} greater than {b}? ({a} > {b})        : {a > b}")
print(f"Is {a} less than {b}? ({a} < {b})           : {a < b}")
print(f"Is {a} greater than or equal to {b}? (>=) : {a >= b}")
print(f"Is {a} less than or equal to {b}? (<=)    : {a <= b}")
print()


print("--- Logical Operations ---")

condition1 = (a > 10)  
condition2 = (b > 10)  

print(f"Condition 1 (a > 10): {condition1}")
print(f"Condition 2 (b > 10): {condition2}")
print(f"Logical AND (condition1 and condition2) : {condition1 and condition2}")
print(f"Logical OR  (condition1 or condition2)  : {condition1 or condition2}")
print(f"Logical NOT (not condition1)            : {not condition1}")

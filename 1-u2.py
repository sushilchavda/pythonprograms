num = int(input("Enter a number: "))

if num > 0:
    print("Using if: Number is positive")

if num % 2 == 0:
    print("Using if: Number is even")

if num >= 0:
    print("Using if-else: Number is non-negative")
else:
    print("Using if-else: Number is negative")

if num > 0:
    print("Using if-elif-else: Number is positive")
elif num < 0:
    print("Using if-elif-else: Number is negative")
else:
    print("Using if-elif-else: Number is zero")

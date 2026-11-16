def generate_numbers(n):
    for i in range(1, n + 1):
        yield i


num = int(input("Enter the limit: "))

print("Generated sequence:")

for number in generate_numbers(num):
    print(number)

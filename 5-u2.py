print("--- Break Statement ---")

for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\n--- Continue Statement ---")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n--- Pass Statement ---")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

# Program to demonstrate seek() and tell() methods

# Create and write data into a file
file = open("student.txt", "w")
file.write("Python Programming")
file.close()

# Open file for reading
file = open("student.txt", "r")

# tell() returns the current position of file pointer
print("Initial position:", file.tell())

# Read first 6 characters
data = file.read(6)
print("Data read:", data)
print("Position after reading:", file.tell())

# Move file pointer to position 7
file.seek(7)
print("Position after seek:", file.tell())

# Read data from position 7
data = file.read()
print("Data after seek:", data)

file.close()

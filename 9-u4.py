# Program to demonstrate different file modes

# Write mode - creates a new file and writes data
file = open("student.txt", "w")
file.write("Name: Sushil\n")
file.write("Course: Python\n")
file.write("Age: 20\n")
file.close()

# Append mode - adds data at the end of the file
file = open("student.txt", "a")
file.write("College: ABC College\n")
file.close()

# Read mode - reads data from the file
file = open("student.txt", "r")
data = file.read()
print("File Content:")
print(data)
file.close()

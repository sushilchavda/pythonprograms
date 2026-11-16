# Program 6: File and Directory Operations

import os
import sys

# Display current working directory
print("Current Directory:", os.getcwd())

# Create a new directory
directory = "TestFolder"

if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory created:", directory)
else:
    print("Directory already exists:", directory)

# Create a file inside the directory
file_path = os.path.join(directory, "sample.txt")

with open(file_path, "w") as file:
    file.write("Hello, Python!")

print("File created:", file_path)

# Check whether file exists
print("File exists:", os.path.exists(file_path))

# Display file size
print("File size:", os.path.getsize(file_path), "bytes")

# Display files and directories
print("\nDirectory contents:")
print(os.listdir("."))

# Display command-line arguments
print("\nCommand-line arguments:")
print(sys.argv)

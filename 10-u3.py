# Program: Extract information from a text file using regular expressions

import re

# Create a text file
with open("data.txt", "w") as file:
    file.write("""
Name: Sushil
Email: sushil@gmail.com
Phone: 9876543210
Age: 20
""")

# Read the file
with open("data.txt", "r") as file:
    text = file.read()

# Extract Email
email = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Extract Phone Number
phone = re.findall(r'\b\d{10}\b', text)

# Extract Age
age = re.findall(r'Age:\s*(\d+)', text)

# Display extracted information
print("Email:", email)
print("Phone:", phone)
print("Age:", age)

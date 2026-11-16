#Write a program to use re module functions
#such as match search and find all.

# Program: Demonstrate match(), search() and findall()

import re

text = "Python is easy to learn. Python is powerful and Python is popular."

# 1. match() - checks for a match at the beginning
result = re.match(r"Python", text)

if result:
    print("match():", result.group())
else:
    print("match(): No match found")


# 2. search() - searches for the first occurrence
result = re.search(r"powerful", text)

if result:
    print("search():", result.group())
else:
    print("search(): No match found")


# 3. findall() - finds all occurrences
result = re.findall(r"is", text)

print("findall():", result)

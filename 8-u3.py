#8. Write a program to demonstrate basic regular
#expression pattern matching.
# Program: Basic Regular Expression Pattern Matching

import re

text = "My phone number is 3474758876 and my email is test@gmail.com."

# Search for a 10-digit phone number
pattern = r"\d{10}"

result = re.search(pattern, text)

if result:
    print("Phone number found:", result.group())
else:
    print("Phone number not found")

# Search for an email address
email_pattern = r"[\w.-]+@[\w.-]+\.\w+"

email = re.search(email_pattern, text)

if email:
    print("Email found:", email.group())
else:
    print("Email not found")

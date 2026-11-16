#Write a program to display current date and
#time using date time module.
# Program: Display Current Date and Time

import datetime

# Get current date and time
current = datetime.datetime.now()

#print("Current Date and Time:", current)
print("Current Date:", current.date())
print("Current Time:", current.time())

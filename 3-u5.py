class AgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18 or above")
    else:
        print("Eligible to vote")

try:
    check_age(20)
    check_age(15)
except AgeError as e:
    print("Error:", e)

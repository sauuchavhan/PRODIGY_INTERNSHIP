import re

def check_password_strength(password):

    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1

    # Number check
    if re.search(r"[0-9]", password):
        strength += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Strength result
    if strength == 5:
        print("Password Strength: Strong")
    elif strength >= 3:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Weak")


# User Input
password = input("Enter your password: ")

# Function Call
check_password_strength(password)
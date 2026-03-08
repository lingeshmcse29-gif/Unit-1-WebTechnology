password = input("Enter your password: ")

length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True

if length < 6:
    print("Password Strength: Weak")
elif length >= 6 and (has_upper or has_lower) and not has_digit:
    print("Password Strength: Medium")
elif length >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Password Strength: Strong")
else:
    print("Password Strength: Moderate")

import random
import string

def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = uppercase + lowercase + digits + symbols

    password = ""

    for i in range(length):
        password += random.choice(all_characters)

    return password


print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
    else:
        password = generate_password(length)
        print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input! Please enter numbers only.")
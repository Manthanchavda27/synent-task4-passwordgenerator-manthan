import random
import string

# Character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = uppercase + lowercase + digits + symbols

# Take user input
length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:", password)
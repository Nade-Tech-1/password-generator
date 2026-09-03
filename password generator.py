import string
import random

length = int(input("Enter password length "))
if length < 8:
    print("password must be at least 8 characters long.")
elif length > 64:
    print("password length cannot exceed 64.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)
    print("Your password is:", password)

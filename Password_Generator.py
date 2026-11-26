import random
import string
print("Welcome to the Password Generator!")
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = int(input("Enter the desired password length:"))
    password = " "
    if password_length < 6:
        print("Password length should be at least 6 characters.")
    else:
        for i in range(password_length):
            password += random.choice(characters)
        return password
print("Generated Password:", generate_password())

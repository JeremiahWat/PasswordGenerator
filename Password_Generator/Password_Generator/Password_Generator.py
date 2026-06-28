import secrets
import string
import random
"""
We use module secrets to generate a secure password, while using random to shuffle the list of characters to ensure randomness.
The password has a minimum length of 12 characters and includes at least one lowercase letter, one uppercase letter, one digit, and one special character.
It uses a while loop to prompt the user for the desired password length, and if the input is invalid, it will ask again until a valid input is provided.
We use a try-except block to handle any invalid input and ensure that the programs does not crash. 
"""
def generate_password(length: int = 12):
    if length < 12:
        print("Password length should be at least 12 characters for better security.")
        return None
    password = []
    password.append(secrets.choice(string.ascii_lowercase))
    password.append(secrets.choice(string.ascii_uppercase))
    password.append(secrets.choice(string.digits))
    password.append(secrets.choice(string.punctuation))
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password.extend(secrets.choice(alphabet) for _ in range(length-4))
    random.SystemRandom().shuffle(password)
    password = "".join(password)
    return password
password = None
while password is None:
    try:
        password_length = int(input("Enter the desired password length (default is 12): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue
    password = (generate_password(password_length))
print(f"Generated password: {password}")
import random
import string

def generate_password(length: int = 12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

password_length = int(input("Enter the desired password length (default is 12): "))
password = (generate_password(password_length))
print(f"Generated password: {password}")
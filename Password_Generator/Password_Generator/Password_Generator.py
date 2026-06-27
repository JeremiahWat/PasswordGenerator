import secrets
import string

def generate_password(length: int = 12):
    if length < 12:
        print("Password length should be at least 12 characters for better security.")
        return False
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password
password = False
while password == False:
    try:
        password_length = int(input("Enter the desired password length (default is 12): "))
    except:
        print("Invalid input. Please enter a valid integer.")
        continue
    password = (generate_password(password_length))
print(f"Generated password: {password}")
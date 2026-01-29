import secrets
import string

letters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(letters) for i in range(12))

print(f"Your new secure password is: {password}")
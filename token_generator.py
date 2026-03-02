# token_generator.py
import secrets

# generate a 32-byte hex secret key
secret_key = secrets.token_hex(32)

# print it to the console
print(secret_key)

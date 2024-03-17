from operator import imatmul
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet cipher instance with the key
cipher_suite = Fernet(key)

# String to encrypt
plain_text = "Hello, world!"

# Encrypt the string
cipher_text = cipher_suite.encrypt(plain_text.encode())

print("Cipher Text:", cipher_text)

# Decrypt the string
decrypted_text = cipher_suite.decrypt(cipher_text).decode()

print("Decrypted Text:", decrypted_text)

import boto3
iam = boto3.client('ec2')
print(iam)

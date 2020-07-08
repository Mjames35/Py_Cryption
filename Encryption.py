from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = input("Input keyword: ")
password = password_provided.encode()
salt = b'\xb3\xca\xbd``\xf9\xeaW\x96\xe3\xa5\x8a\xa4\xa2B\x16'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))


input_file = input("Select a .txt input file name: ")
output_file = input("Select a .txt output file name: ")

with open(input_file, "rb") as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, "wb") as f:
    f.write(encrypted)



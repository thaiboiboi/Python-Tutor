# Application of hashing in securing passwords

# Method sha512 from module hashlib is a cryptographic
# hash function developed by the NSA (National Security Agency).
# "sha" refers to "secure hash algorithm"
from hashlib import sha512
# Method uuid4 from module uuid generates a random
# "universally unique identifier"
from uuid import uuid4

# This function applies sha512 to a salted password:
def hash_pw_with_salt(password, salt):
    return sha512(salt.encode() + password.encode()).hexdigest()

# This function encrypts a password to a unique cypher:
def encrypt_pw(password):
    salt = uuid4().hex
    hashed_pw_with_salt = hash_pw_with_salt(password, salt)
    return hashed_pw_with_salt + ':' + salt

# This function verifies a given password with an earlier encrypted
# password:
def verify_pw(encrypted_pw_with_salt, new_password):
    hashed_pw_with_salt, salt = encrypted_pw_with_salt.split(':')
    hashed_new_pw_with_salt = hash_pw_with_salt(new_password, salt)
    return hashed_pw_with_salt == hashed_new_pw_with_salt

# This function prints a string in a fixed number of characters per
# line:
def print_large_string(string, number):
    n = len(string)
    i = 0
    while i < n:
        print(string[i:i + number])
        i += number

password1 = input("Enter your password: ")
encrypted_password_with_salt = encrypt_pw(password1)
print("The encrypted password:")
print_large_string(encrypted_password_with_salt, 64)
password2 = input("Enter the password again: ")
if verify_pw(encrypted_password_with_salt, password2):
    print("The password is correct")
else:
    print("The password is not correct")

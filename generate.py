#! python

import random
import string
import pyperclip

def generate_password(length):
    # Get all the printable ASCII characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use random.sample to get a list of random characters of the desired length
    password = "".join(random.sample(characters, length))
    return password

# Generate a random password of length 10
password = generate_password(10)

# Copy the password to the clipboard
pyperclip.copy(password)
print("Password copied to clipboard: " + password)

input("Press Ctrl+C to exit")

for i in range():
    print("git")

import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

a = 1 
b = 2
for i in range(5):
    print(1+2)
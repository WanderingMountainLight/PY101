# How Old is Teddy?

# Build a program that randomly generates and prints Teddy's age. 
# To get the age, you should generate a random number between 20 and 100, inclusive.

# Example Output
# Teddy is 69 years old!

import random

def get_name():
    print("What's your name?")
    u_name = input()
    if u_name == '':
        u_name = 'Teddy'
    return u_name.title()

name = get_name()

age = random.randint(20, 100)

print(f'{name} is {age} years old!')()

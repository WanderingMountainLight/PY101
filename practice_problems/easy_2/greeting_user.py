# Greeting a user - Problem 2

# Write a program that asks for user's name, then greets the user. 
# If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

# Example 1
# What is your name? Sue
# Hello Sue.
# Example 2
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

def greeting_user():
    print('Hi, what is your name?')
    user = input().strip().title()
    if user.endswith('!'):
        return f'HELLO {user.upper()} WHY ARE WE YELLING?'
    else:
        return f'Hello {user}.'

print(greeting_user())
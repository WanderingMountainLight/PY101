# Write a function that takes two arguments,
# a string and a positive integer,
# then prints the string as many times as the integer indicates.

# Example
# repeat('Hello', 3)
# Output
# Hello
# Hello
# Hello

def repeat(str, num):
    count = 0
    while count < num:
        print(str)
        count += 1


repeat('Hello', 3)
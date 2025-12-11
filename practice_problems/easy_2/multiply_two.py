# Multiplying Two Numbers - Problem 3

# Create a function that takes two arguments, multiplies them together, and returns the result.

# Example
# print(multiply(5, 3) == 15)  # True

def multiply(x, y):
    return x * y

print(multiply(5, 3) == 15)

# Squaring an Argument

# Using the multiply function from the "Multiplying Two Numbers" exercise, 
# write a function that computes the square of its argument 
# (the square is the result of multiplying a number by itself).

# Examples
# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

def square(n):
    return multiply(n ,n)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

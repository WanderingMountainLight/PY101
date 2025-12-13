# Stringy Strings

# Write a function that takes one argument, a positive integer, 
# and returns a string of alternating '1's and '0's, always starting with a '1'. 
# The length of the string should match the given integer.

# Examples
# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

def stringy(num):
    lst = []
    for n in range(num):
        if n % 2 == 0:
            lst.append(1)
        else:
            lst.append(0)
        numbers = lst.pop()
    return numbers
            



print(stringy(6))# == "101010")
# Get Middle Character

# Write a function that takes a non-empty string argument and returns the middle character(s)
# of the string. If the string has an odd length, you should return exactly one character.
# If the string has an even length, you should return exactly two characters.

# ExamplesCopy Code
# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True

# def center_of(str):
#     new_str = str.replace(' ', '')
#     length = len(new_str)
#     mid = length // 2
#     if length % 2 == 0:
#         return (new_str[mid -1] + new_str[mid])
#     return str[mid]
# This works if we want just characters not spaces.


# print(center_of('I Love Python!!!'))

def center_of(str):
    length = len(str)
    mid = length // 2
    if length % 2 == 0:
        return (str[mid -1] + str[mid])
    else:
        return str[mid]



print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
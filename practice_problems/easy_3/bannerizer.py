# Bannerizer

# Write a function that takes a short line of text and prints it within a box.

# Example 1
# print_in_box('To boldly go where no one has gone before.')
# Output for Example 1
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+
# Example 2
# print_in_box('')
# Output for Example 2
# +--+
# |  |
# |  |
# |  |
# +--+
# You may assume the output will always fit in your terminal window.


def print_in_box(str):
    width = len(str) + 2
    print('+' + ('-' * width) + '+')
    print('|'+(' ' * width)+'|')
    print('|'+(' ' + str + ' ')+'|')
    print('|'+(' ' * width) +'|')
    print('+'+('-' * width)+'+')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')

# Further Exploration

# Modify this function so that it truncates the message if it doesn't fit inside
# a maximum width provided as a second argument (the width is the width of the box itself). 
# You may assume no maximum if the second argument is omitted.

# For a challenging but fun exercise, 
# try word wrapping messages that are too long to fit, 
# so that they appear on multiple lines but are still contained within the box. 
# This isn't an easy problem, but it's doable with basic Python.

def print_in_box(message, width=None):
    message_length = len(message)
    max_width = width

    if max_width == None:
        max_width = len(message) + 2

    if message_length > max_width:
        message = message[:(max_width - 4)]

    message_length = len(message)
    horizontal_rule = f'+-{"-" * message_length}-+'
    empty_line = f'| {" " * message_length} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)

print_in_box('To boldly go where no one has gone before.', 20)
print_in_box('')

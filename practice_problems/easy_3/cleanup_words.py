# Clean up the words

# Given a string that consists of some words and an assortment of non-alphabetic characters, 
# write a function that returns that string with all of the non-alphabetic characters replaced by spaces. 
# If one or more non-alphabetic characters occur in a row, you should only have one space in the result
# (i.e., the result string should never have consecutive spaces).

# Example
# print(clean_up("---what's my +*& line?") == " what s my line ")
# # True

def clean_up(str):
    new_str = []
    for n in str:
        if n.isalpha():
            new_str.append(n)
        else:
            if new_str and new_str[-1] == ' ':
                pass
            else:
                new_str.append(' ')
    return ''.join(new_str)

print(clean_up("---what's my +*& line?") == " what s my line ")
# True


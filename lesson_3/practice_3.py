#Question 1
#Write two different ways to remove all of the elements from the following list:

numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)

del numbers[:]
print(numbers)

#Question 2
#What will the following code output?

print([1, 2, 3] + [4, 5])

#Try to answer without running the code.

#This will print [1, 2, 3, 4, 5] (Correct)

#Question 3
#What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

#Try to answer without running the code.
#This will print hello there (Correct)

#Question 4
#What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

#Try to answer without running the code.

#This will print [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
#becasue my_list1 wasn't mutated. (Incorrect)
#Because my_list2 is a direct copy of my_list1,
#when my_list2 is mutated, it updates and mutates
#my_list1 to [{'first': 42}, {'second': 'value2'}, 3, 4, 5]

#Question 5
#The following function unnecessarily uses two return 
#statements to return boolean values. 
#Can you rewrite this function so it only has one return statement
#and does not explicitly use either True or False?

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
#Try to come up with two different solutions.

color = 'blue'

def is_color_valid(color):
    return color == "blue" or color == "green"

is_color_valid(color)

color = 'blue'

def is_color_valid(color):
    valid_colors = ['blue', 'green']
    return color in valid_colors

is_color_valid(color)
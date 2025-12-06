
#Question 1
#Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

numbers.reverse()

print(numbers)

reversed_numbers = numbers[::-1]

print(reversed_numbers)

# Question 2
# Given a number and a list, determine whether the number 
# is included in the list.

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

#Question 3
#Programmatically determine whether 42 lies between 10 and 100, inclusive. 
#Do the same for the values 100 and 101.

print(42 in range(10, 100))
print(100 in range(10, 101))
print(101 in range(10, 101))

#Question 4
#Given a list of numbers [1, 2, 3, 4, 5],
#mutate the list by removing the number at index 2,
#so that the list becomes [1, 2, 4, 5].

numbers = [1, 2, 3, 4, 5]

new_numbers = numbers.pop(2)

print(numbers)

#Question 5
#How would you verify whether the data structures assigned to the variables
#numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers))
print(type(table))

#Question 6
#Back in the stone age (before CSS), we used spaces to align things on the screen.
#If we have a 40-character wide table of Flintstone family members,
#how can we center the following title above the table with spaces?

title = "Flintstone Family Members"

centered = f'{title:^40}'

print(centered)

words = 'hello from the magic tavern'

print(words.center(40))

#Question 7
#Write a one-liner to count the number of lower-case t characters in each
# of the following strings:

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'))
print(statement2.count('t'))

#Question 8
#Determine whether the following dictionary of people
#and their age contains an entry for 'Spot':

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print('spot' in ages)

#Question 9
#We have most of the Munster family in our ages dictionary:

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

#Add entries for Marilyn and Spot to the dictionary:

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)

print(ages)
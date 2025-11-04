#-Ask the user for the first number
#-Ask the user for the second number
#-Ask the user for an operation to perform
#-Perform the operation on the two numbers
#-Print the result to the Terminal

print('Welcome to Calculator!')

print('Please provide the first number.')
number1 = input()
print('Please provide the second number.')
number2 = input()

print('What operation would you like to perform?\n'
        '1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()


if operation == '1': # '1' represents Addition
    result = int(number1) + int(number2)
elif operation == '2': # '2' represents Subtraction
    result = int(number1) - int(number2)
elif operation == '3': # '3' represents Multiplication
    result = int(number1) * int(number2)
elif operation == '4': # '4' represents Division
    result = int(number1) / int(number2)
print(f'The result is {result}.')
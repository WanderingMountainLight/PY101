def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

continue_cal = True

while continue_cal:
    prompt('Please provide the first number.')
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()
    prompt('Please provide the second number.')
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()

    prompt("""What operation would you like to perform?
        1) Add 2) Subtract 3) Multiply 4) Divide""")
    operation = input()

    while operation not in ['1', '2', '3','4']:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    match operation:
        case '1': # '1' represents Addition
            result = float(number1) + float(number2)
        case '2': # '2' represents Subtraction
            result = float(number1) - float(number2)
        case '3': # '3' represents Multiplication
            result = float(number1) * float(number2)
        case '4': # '4' represents Division
            result = float(number1) / float(number2)
    prompt(f'The result is {result}.')
    prompt("""Would you like to perform another calculation?
           Yes or No""")
    answer = input()
    answer_str = answer.title()
    print(answer_str)
    while answer_str not in ['Yes', 'No']:
        prompt("That's not a valid input. Please choose 'Yes' or 'No'.")
        answer = input()
        answer_str = answer.title()

    if answer_str == 'Yes':
        continue_cal = True
    elif answer_str == 'No':
        continue_cal = False
        prompt('Thank you for using calculator')
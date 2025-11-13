import json

with open('calculator_messages.json', 'r') as file:
    messages = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

prompt(messages['welcome'])

continue_cal = True

while continue_cal:
    prompt(messages['first_num'])
    number1 = input()

    while invalid_number(number1):
        prompt(messages['invalid_num'])
        number1 = input()
    prompt(messages['second_num'])
    number2 = input()

    while invalid_number(number2):
        prompt(messages['invalid_num'])
        number2 = input()

    prompt(messages['choose_operation'])
    operation = input()

    while operation not in ['1', '2', '3','4']:
        prompt(messages['invalid_operation'])
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
    prompt(messages['another_calc'])
    answer = input()
    answer_str = answer.title()
    
    while answer_str not in ['Yes', 'No']:
        prompt(messages['invalid_yes_no'])
        answer = input()
        answer_str = answer.title()

    if answer_str == 'Yes':
        continue_cal = True
    elif answer_str == 'No':
        continue_cal = False
        prompt(messages['thank_you'])
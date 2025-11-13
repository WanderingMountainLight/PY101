import json

with open('calculator_messages.json', 'r') as file:
    all_messages = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

prompt("Select language: 1) English 2) Espanol 3) Português")
lang_choice = input()

while lang_choice not in ['1', '2', '3']:
    prompt('Invalid choice. Please select 1, 2, or 3')
    lang_choice = input()

if lang_choice == '1':
    LANG = 'english'
elif lang_choice == '2':
    LANG = 'spanish'
elif lang_choice == '3':
    LANG = 'portuguese'

messages = all_messages[lang_choice]


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

    while answer_str not in [messages['yes_response'],
                             messages['no_response']]:
        prompt(messages['invalid_yes_no'])
        answer = input()
        answer_str = answer.title()

    if answer_str == messages['yes_response']:
        continue_cal = True
    elif answer_str == messages['no_response']:
        continue_cal = False
        prompt(messages['thank_you'])
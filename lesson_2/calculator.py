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

def prompt_for_num(prompt_message, error_message):
    prompt(prompt_message)
    num = input()

    while invalid_number(num):
        prompt(error_message)
        num = input()

    return num


def operation_choice(num1, num2, msg):
    prompt(msg['choose_operation'])
    operation_num = input()

    while operation_num not in ['1', '2', '3','4']:
        prompt(msg['invalid_operation'])
        operation_num = input()

    if operation_num == '4':
        while invalid_number(num2) or float(num2) == 0:
            if invalid_number(num2):
                prompt(msg['invalid_num'])
                num2 = input()
            else:
                prompt(msg['divide_by_zero'])
                num2 = input()

    match operation_num:
        case '1': # '1' represents Addition
            calculation_result = float(num1) + float(num2)
        case '2': # '2' represents Subtraction
            calculation_result = float(num1) - float(num2)
        case '3': # '3' represents Multiplication
            calculation_result = float(num1) * float(num2)
        case '4': # '4' represents Division
            calculation_result = float(num1) / float(num2)

    return calculation_result

def main():
    prompt("Select language: 1) English 2) Espanol 3) Português")
    lang_choice = input()

    while lang_choice not in ['1', '2', '3']:
        prompt('Invalid choice. Please select 1, 2, or 3')
        lang_choice = input()

    if lang_choice == '1':
        lang = 'english'
    elif lang_choice == '2':
        lang = 'spanish'
    else:
        lang = 'portuguese'

    messages = all_messages[lang]

    prompt(messages['welcome'])

    continue_calc = True

    while continue_calc:
        number1 = prompt_for_num(messages['first_num'],
                                 messages['invalid_num'])

        number2 = prompt_for_num(messages['second_num'],
                                 messages['invalid_num'])

        result = operation_choice(number1, number2, messages)

        prompt(f'The result is {result}.')

        prompt(messages['another_calc'])
        answer = input()
        answer_str = answer.title()

        while answer_str not in [messages['yes_response'],
                                messages['no_response']]:
            prompt(messages['invalid_yes_no'])
            answer = input()
            answer_str = answer.title()

        if answer_str == messages['no_response']:
            continue_calc = False
            prompt(messages['thank_you'])

main()
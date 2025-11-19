"Mortgage Calculator"

def prompt(message):
    """Display a formatted message to the user"""
    print(f'===> {message}')

def is_valid_num(num):
    """Validates number input"""
    try:
        float(num)
        return True
    except ValueError:
        return False

def cleaned_input(text):
    """Cleans input text"""
    clean_value = text.replace(",", "").replace("$", "").replace("%", "")
    return clean_value

def more_than_zero(prompt_message):
    """Validates user input, and loops if invaild input"""
    prompt(prompt_message)
    user_input = input().strip()
    user_input = cleaned_input(user_input)
    while not is_valid_num(user_input) or float(user_input) <= 0:
        prompt('Invalid input value. Please input a numerical value.')
        user_input = input().strip()
        user_input = cleaned_input(user_input)
    return float(user_input)

def months_or_years(user_term_string):
    """Prompts user for term of loan"""
    prompt(user_term_string)
    user_term_string = input().strip().title()
    while user_term_string not in ['Months', 'Years']:
        prompt('Invaild input value. Please input Months or Years')
        user_term_string = input().strip().title()
    if user_term_string == 'Months':
        user_term = more_than_zero('How many months?')
    else:
        user_term = more_than_zero('How many years?') * 12
    return user_term

def calc_monthly(value, apr, time):
    """Monthly payment calculation"""
    apr = apr / 100
    apr = apr / 12
    monthly = (value * (apr / (1 - (1 + apr) ** (-time))))
    return monthly

def main():

    prompt('Welcome to my mortgage calculator.')

    calc_loan = True

    while calc_loan:

        principle = more_than_zero('What is your principle amount?')

        interest_rate = more_than_zero(
            'What is your interest rate? (Ex: 5 for 5%)'
            )

        term = months_or_years(
            'Is your loan measured in Months or Years?'
            )

        monthly_payment = calc_monthly(principle, interest_rate, term)

        prompt(f'Your principle is: ${principle}')
        prompt(f'Your interst rate is: {interest_rate}%')
        prompt(f'Your monthly payment is: ${monthly_payment:.2f}')
        prompt('Would you like to calculate another loan option? Yes or No')

        answer = input().strip().title()

        while answer not in ['Yes', 'No']:
            prompt('This is not a valid answer. Please answer: Yes or No.')
            answer = input().strip().title()

        if answer == 'No':
            prompt('Thank you for using my loan calculator!')
            calc_loan = False

main()

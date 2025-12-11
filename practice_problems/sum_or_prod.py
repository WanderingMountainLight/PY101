def valid_input(num):
    try:
        int(num)
        return True
    except (ValueError, TypeError):
        return False

def valid_number():
    num = input().strip()
    while not valid_input(num) or int(num) <= 0:
        print("That's not a valid input. Please input a number greater than zero")
        num = input()
    return num

def calc_sum_or_prod():

    print('Please enter an integer greater than 0:')

    integer = valid_number()

    print(f'Would you like a sum or product of the numbers between 1 and {integer}?')

    user_choice = input().strip().lower()

    if user_choice == 'sum':
        user_sum = 0
        number = 1

        while number <= int(integer):
            user_sum = user_sum + number
            number += 1
        return user_sum
    
    if user_choice == 'product':
        total = 1
        number = 1

        while number <= int(integer):
            total = total * number
            number += 1
        return total

print(calc_sum_or_prod())
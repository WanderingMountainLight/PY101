def valid_input(num):
    try:
        float(num)
        return True
    except (ValueError, TypeError):
        return False
    
def get_valid_number():
    number = input()
    while valid_input(number) == False:
        print("that's not a valid input. Please input a number.")
    if valid_input == True:    
        return float(number)


def bill_calc():
    print('What is the bill?')
    total = get_valid_number()

    print('What percentage would you like to tip?')
    tip = get_valid_number()
   

    # while not valid_input(tip):
    #     print("That's not a valid input. Please input a number.")
    #     tip = input()
    tip_amount = (float(tip)/ 100) * total

    print(f'The tip is ${tip_amount:.2f}')
    print(f'The total bill is ${tip_amount + total:.2f}')
    
    

bill_calc()

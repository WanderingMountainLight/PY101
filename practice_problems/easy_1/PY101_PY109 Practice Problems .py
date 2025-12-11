
#Problem 3
n = 1

for n in range(1, 100, 2):
    count = 0
    n = n + count
    count += 2
    print(n)


for number in range(2,100, 2):
    # if number % 2 == 0:
        print(number)

#Problem 4

def room_size(length, width):
    length_meter = length / 3.28
    width_meter = width / 3.28
    return (f'The room is {length * width:.2f} square feet or {length_meter * width_meter:.2f} square meters.')

print('What is the length of the room in feet?')
length = float(input())
print('What is the width of the room in feet?')
width = float(input())

print(room_size(length, width))

def meters_or_feet():
    print('Would you like to measure in meters or feet today?')
    user_selection = input().strip().lower()
    if user_selection == 'meters':
        print('What is the length of the room?')
        len_m = float(input())
        print('What is the width of the room?')
        width_m = float(input())
        sqm = len_m * width_m
        return (f'The total square meters of the room is {sqm:.2f} or {sqm * 10.7639:.2f} square feet')
        
    elif user_selection == 'feet':
        print('What is the length of the room?')
        len_ft = float(input())
        print('What is the width of the room?')
        width_ft = float(input())
        sqft = len_ft * width_ft
        
    return (f'The total square footage of the room is {sqft:.2f} or {sqft / 10.7639:.2f} square meters')

print(meters_or_feet())

#Problem 5

def valid_input(num):
    try:
        float(num)
        return True
    except (ValueError, TypeError):
        return False
    
def get_valid_number():
    number = input()
    while not valid_input(number):
        print("that's not a valid input. Please input a number.")
        number = input()
    return float(number)


def bill_calc():
    print('What is the bill?')
    total = get_valid_number()

    print('What percentage would you like to tip?')
    tip = get_valid_number()
   
    tip_amount = (tip/ 100) * total

    print(f'The tip is ${tip_amount:.2f}')
    print(f'The total bill is ${tip_amount + total:.2f}')
    
    

bill_calc()

#Problem 6
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

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

def calc_sum_or_prod(choice, number):

    if choice == 'sum':
        user_sum = 0
        x = 1

    while x <= int(number):
        user_sum = user_sum + x
        x += 1
        return user_sum
    
    if choice == 'product':
        total = 1
        x = 1

    while x <= int(number):
        total = total * x
        x += 1
        return total

print('Please enter an integer greater than 0:')

integer = valid_number()

print(f'Would you like a sum or product of the numbers between 1 and {integer}?')

user_choice = input().strip().lower()

total = calc_sum_or_prod(user_choice, integer)

print(total)
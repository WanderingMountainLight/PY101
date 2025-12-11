# Floating Point Arithmetic

# Write a program that prompts the user for two positive numbers (floating-point),
# then prints the results of the following operations on those two numbers: 
# addition, subtraction, product, quotient, floor quotient, remainder, and power. 
# Do not worry about validating the input.

# Examples
# ==> Enter the first number:
# 3.141592
# ==> Enter the second number:
# 2.718282
# ==> 3.141592 + 2.718282 = 5.859874
# ==> 3.141592 - 2.718282 = 0.4233100000000003
# ==> 3.141592 * 2.718282 = 8.539732984944001
# ==> 3.141592 / 2.718282 = 1.1557270364149121
# ==> 3.141592 // 2.718282 = 1.0
# ==> 3.141592 % 2.718282 = 0.4233100000000003
# ==> 3.141592 ** 2.718282 = 22.45914942746313


print('==> Enter the first number: ')
first_number = float(input())

print('==> Enter the second number: ')
second_number= float(input())

print(f'==> {first_number} + {second_number} = {first_number + second_number}')
print(f'==> {first_number} - {second_number} = {first_number - second_number}')
print(f'==> {first_number} * {second_number} = {first_number * second_number}')
print(f'==> {first_number} / {second_number} = {first_number / second_number}')
print(f'==> {first_number} // {second_number} = {first_number // second_number}')
print(f'==> {first_number} % {second_number} = {first_number % second_number}')
print(f'==> {first_number} ** {second_number} = {first_number ** second_number}')
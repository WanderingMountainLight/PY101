import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'===> {message}')

def display_winner(player, computer):
    if((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        prompt('You win')
    elif((player == 'rock' and computer == 'paper') or
        (player == 'paper' and computer == 'scissors') or
        (player == 'scissors' and computer == 'rock')):
        prompt('Computer wins')
    else:
        prompt("It's a tie!")

while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt(f'''That is not a vaild choice.
               Please choose one: {', '.join(VALID_CHOICES)}''')
        choice = input()

    cpu_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}. The computer chose {cpu_choice}.')

    display_winner(choice, cpu_choice)

    prompt("Would you like to play again? (y/n)")
    answer = input().lower()

    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n"')
        answer = input().lower()

    if answer[0] == 'n':
        prompt('Thanks for playing!')
        break
import random


user_count = 0
cpu_count = 0

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'===> {message}')

def display_winner(player, computer):
    if((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        prompt('You win')
        return 'You win'
    elif((player == 'rock' and computer == 'paper') or
        (player == 'paper' and computer == 'scissors') or
        (player == 'scissors' and computer == 'rock')):
        prompt('Computer wins')
        return 'Computer wins'
    else:
        return "It's a tie!"

def games_won(winner):
    global user_count, cpu_count
    if winner == 'You win':
        user_count += 1
        prompt(f'You have won {user_count} games.')
        return user_count
    elif winner == 'Computer wins':
        cpu_count += 1
        prompt(f'The computer has won {cpu_count} games.')
        return cpu_count
    else:
        prompt("It's a tie. Let's try again!")
    
def score_message(result):
    global user_count, cpu_count
    if result == 'You win':
        if user_count < 5:
            prompt(f'''You won that round.
                The current score is: 
                User {user_count} games.
                Computer {cpu_count} games.
                Whomever wins 5 first, wins the match''')
            return True
        else:
            prompt(f'''You won.
                Final score:
                User {user_count}
                Computer {cpu_count}''')
            return False
            
    elif result == 'Computer wins':
        if cpu_count < 5:
            prompt(f'''You lost that round.
                The current score is: 
                User {user_count} games.
                Computer {cpu_count} games.
                Whomever wins 5 first, wins the match''')
            return True
        else:
            prompt(f'''You Lost.
                Final score:
                Computer {cpu_count}
                User {user_count}''')
            return False
    else:
        prompt(f'''The current score is: 
                User {user_count} games.
                Computer {cpu_count} games.
                Whomever wins 5 first, wins the match''')
        return True

def main():
    while True:

        prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
        choice = input()

        while choice not in VALID_CHOICES:
            prompt(f'''That is not a vaild choice.
                Please choose one: {', '.join(VALID_CHOICES)}''')
            choice = input()

        cpu_choice = random.choice(VALID_CHOICES)

        prompt(f'You chose {choice}. The computer chose {cpu_choice}.')

        result = display_winner(choice, cpu_choice)
        
        games_won(result)

        keep_playing = score_message(result)

        if keep_playing == False:
            break

while True:
    main()

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
    elif answer[0] == 'y':
        user_count = 0
        cpu_count = 0

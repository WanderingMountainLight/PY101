import random


user_count = 0
cpu_count = 0

VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    'sci': 'scissors',
    'liz': 'lizard',
    'spo': 'spock'}

WINNING_COMBOS = {
    'rock' : ['lizard','scissors'],
    'paper' : ['rock', 'spock'],
    'scissors' : ['paper', 'lizard'],
    'lizard' : ['spock', 'paper'],
    'spock' : ['scissors', 'rock']
}

def prompt(message):
    print(f'===> {message}')

def display_winner(player, computer):
    if computer in WINNING_COMBOS[player]:
        prompt('You win')
        return 'You win'
    if player in WINNING_COMBOS[computer]:
        prompt('Computer wins')
        return 'Computer wins'
    return "It's a tie!"

def games_won(winner):
    global user_count, cpu_count
    if winner == 'You win':
        user_count += 1
        prompt(f'You have won {user_count} games.')
    if winner == 'Computer wins':
        cpu_count += 1
        prompt(f'The computer has won {cpu_count} games.')
    prompt("It's a tie. Let's try again!")

def score_message(result):
    if result == 'You win':
        if user_count < 5:
            prompt(f'''You won that round.
                The current score is: 
                User {user_count} games.
                Computer {cpu_count} games.
                Whomever wins 5 first, wins the match''')
            return True
        prompt(f'''You won.
            Final score:
            User {user_count}
            Computer {cpu_count}''')
        return False

    if result == 'Computer wins':
        if cpu_count < 5:
            prompt(f'''You lost that round.
                The current score is: 
                User {user_count} games.
                Computer {cpu_count} games.
                Whomever wins 5 first, wins the match''')
            return True
        prompt(f'''You Lost.
            Final score:
            Computer {cpu_count}
            User {user_count}''')
        return False
    prompt(f'''The current score is:
            User {user_count} games.
            Computer {cpu_count} games.
            Whomever wins 5 first, wins the match''')
    return True

def main():
    prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')

    while True:

        choices_list = []
        for shortcut, full_name in VALID_CHOICES.items():
            choices_list.append(f"{shortcut} for {full_name.title()}")
        choices_string = ", ".join(choices_list)

        prompt(f"Choose one: {choices_string}")
        user_choice = input()

        while user_choice not in VALID_CHOICES:
            prompt(f'That is not a valid choice. Choose one: {choices_string}')
            user_choice = input()

        user_choice = VALID_CHOICES[user_choice]

        cpu_choice = random.choice(list(VALID_CHOICES.values()))

        prompt(f'You chose {user_choice}. The computer chose {cpu_choice}.')

        result = display_winner(user_choice, cpu_choice)

        games_won(result)

        keep_playing = score_message(result)

        if not keep_playing:
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
    user_count = 0
    cpu_count = 0

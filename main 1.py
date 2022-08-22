from colors import *
from random import randint


def welcome_Screen():
    print(BLUE, '**** Welcome To Your World Of Guessing *****')
    user_input = int(input(WHITE + 'make a guess)\n'
                                   '1. Normal (1 - 50)\n'
                                   '2. Intermediate (1 - 200)\n'
                                   '3. Hard (1 - 500)\n'
                                   '4. Exit))\n\n'
                                   'Enter Request : '))
    #  calling a function and passing user_input to it
    guess_range = User_Option(user_input)
    if guess_range != 0:
        generate_random_number(guess_range)


# User Option:
def User_Option(user_input):
    guess_range = 0
    if user_input == 1:
        guess_range = 50
    elif user_input == 2:
        guess_range = 200
    elif user_input == 3:
        guess_range = 500
    elif user_input == 4:
        print('**** Hope you enjoyed guessing?, see you later ****')
        exit(1)
    else:
        print(RED, 'Invalid Request, Try again')
        welcome_Screen()
    return guess_range


def generate_random_number(guess_range):
    #  Generate random number between certain range
    generate_number = randint(1, guess_range)

    # user chances
    user_limit = 4

    for i in range(4):
        user_input = int(input('Guess : '))
        if user_input == generate_number:
            print(GREEN, f'Congratulation!, You made the right guess')
            break
        elif user_input > generate_number:
            print(YELLOW, 'You guess too high, Try again')
        elif user_input < generate_number:
            print(YELLOW, 'Your Guess Is Too Low, Try Again')

        #         reduce the user chances and prompt user chances left
        user_limit -= 1
        print(f'Number of chance left is {user_limit}')
        print('Sorry, You failed!')

    #  inform user of the correct guess number
    if user_limit == 0:
        print(f'The correct guess is {generate_number}')


welcome_Screen()

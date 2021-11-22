# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Lists for the game functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
color_list_one = ['red', 'green', 'orange', 'pink']
color_list_two = ['blue', 'yellow', 'purple', 'brown']

print('Welcome to the game of "Loppan".\n')


def print_menu():
    """
    The first a user ses when entering the terminal.
    Prints the menu options for the user.
    """
    print('[1] About Game')
    print('[2] Play Game')
    print('[3] Create Your Own "Loppa"')
    print('[0] Exit Game')


def about_game():
    """
    Will print information about the Game for the user
    """
    print('Handle option "About Game"\n')


def play_game():
    """
    Will Print rules and start the game for the user.
    """
    print('Handle option "Play Game"\n')


def create_own():
    """
    Will print information about how the user can make their own 'Loppa'
    """
    print('Handle option \'Create Your Own "Loppa"\'\n')


def exit_game():
    """
    The user will exit the game
    """
    print('Exit Game \n')


while True:
    print_menu()
    option = ''
    try:
        option = int(input('Where do you want to go? Enter number here: '))
    except ValueError as e:
        print(f'Invalid data: {e}, try again.\n')

    if option == 1:
        about_game()
    elif option == 2:
        play_game()
    elif option == 3:
        create_own()
    elif option == 0:
        exit_game()
        break
    else:
        print('Please chose a number between 0 and 3')


print('Thank you for visiting "Loppan". Please comeback again')

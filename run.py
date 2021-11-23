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
    print("""
    About the Game Loppan
    Loppan is the Swedish name for the childrens game: fortune teller,
    cootie catcher, chatterbox, salt cellar, whirlybird, or paku-paku.
    Loppan is a form of origami and made out of paper. The loppa are labeled
    with colors and/or numbers.
    These serve as an option for the player to choose. Inside each label,
    there is a message or a task for the player to execute.
    The person operating the loppa manipulates the device based on the choices
    made by the player, often folding the loppa a certain amount of time
    and then revealing one of the hidden messages chosen by the player.
    """)


def play_game():
    """
    Will Print rules and start the game for the user.
    """
    print('Handle option "Play Game"\n')


def create_own():
    """
    Will print information about how the user can make their own 'Loppa'
    """
    print("""
    Create Your Own
    To make a Loppa/fortune teller, you need:
        * a piece of A4 paper or a squared shape paper
        * scissor
        * pencils

    Instructions:
    1. Fold the corners of a sheet of paper so they meet up
        on the opposite sides.
        If the paper is not a square, cut the top off,
        making it a square sheet with diagonal creases.

    2. Fold the four corners of the square into the center,
        forming a shape known in origami terminology as a
        blintz base or cushion fold.
        Turn the paper square over,
        and fold the four corners into the middle a second time.

    3. The top of the square should look like a squared cake with 8 slices.
        On each slice, you can put a number or a color.
        Open up one of the corners at a time and write a fortune
        or a task under each slice.

    4. When done, it should look like a folded cushion,
        as at the end of step 2.
        Work your fingers into the pockets on the backside of the cushion,
        all the way into the four corners.
    """)


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

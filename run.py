# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Lists for the game functions
import random

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
color_list_one = ['red', 'green', 'orange', 'pink']
color_list_two = ['blue', 'yellow', 'purple', 'brown']

print('Welcome to the game of "Loppan".\n')


def get_player_num():
    """
    Get the number input from the player.
    Run a while loop to collect the valid number from the user,
    that must be a number between 1 to 10. The loop will request
    data until the user input is valid.
    """
    print("""
Loppan will test your mathematical skills.
Follow the instruction provided. Let's start!

    """)

    print('Please choose a number between 1 to 10.')
    number = []
    while True:
        try:
            get_num = input('Enter your number here:\n')

            player_num = int(get_num)

            if player_num > 0 and player_num < 11:
                print(f'Your choice is {player_num}')
                number.append(player_num)
                break
            else:
                print('Please choose a valid number.')
                continue
        except ValueError:
            print('Not a number: please try again.\n')
            continue
    get_color_list(player_num)


def get_color_list(player_num):
    """
    Get a list of colors displayed in terminal.
    Check if number input value is an even or odd number,
    print differnet list depending on number.
    """
    if player_num % 2 == 0:
        print('Choose a color:')
        print(color_list_one)
        get_color(color_list_one)
    else:
        print('Choose a color:')
        print(color_list_two)
        get_color(color_list_two)


def get_color(color_list):
    """
    Get a color input from the player.
    Checks if the input value matches with options,
    if input is valid, runs a math function.
    """
    try:
        player_color = input('Enter your color choice:\n')
        if player_color in color_list:
            for index, color in enumerate(color_list):
                if color == player_color:
                    print(f'Your choice is {player_color}.\n')
                    # math_quest(index)
        else:
            print(f'{player_color} is not a valid color, try again.\n')
    except ValueError:
        print(f'{player_color} is not a valid color, please try again.\n')


def math_quest(index):
    """
    Get the player a math equation to solve,
    depending on value from get_color function.
    """
    operator = ['+', '-', '*', '/']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    if index == 0:
        first, second = num1, num2
        answer = num1+num2
    elif index == 1:
        if num1 > num2:
            first, second = num1, num2
        else:
            first, second = num2, num1
        answer = first - second
    elif index == 2:
        first, second = num1, num2
        answer = num1*num2
    elif index == 3:
        num1 = num1*num2
        first, second = num1, num2
        answer = int(first/second)

    print('What is ', first, operator[index], second, '?')
    # return answer
    get_answer(answer)


def get_answer(answer):
    """
    Let player submit answer.
    The input value has to be an integer.
    Check if answer provided is correct or incorrect.
    """
    player_answer = int(input('Enter your answer here: '))

    if player_answer == answer:
        print(f'Hooray! {answer} is the right answer\n')
    else:
        print(f'Oh no, you got this one wrong! Its {answer}')


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
    get_player_num()


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


def main():
    """
    The main function of the program.
    """
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Where do you want to go? Enter number:\n'))
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


main()

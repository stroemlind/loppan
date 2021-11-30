# Lists for the game functions
import random
import time
import os
import sys
from os import system, name


def clear():
    """"
    Clears the terminal from clogging up
    """
    os.system("cls" if os.name == "nt" else "clear")


color_list_one = ['red', 'green', 'orange', 'pink']
color_list_two = ['blue', 'yellow', 'purple', 'brown']
lives = 3


def get_player_num(lives):
    """
    Get the number input from the player.
    Run a while loop to collect the valid number from the user,
    that must be a number between 1 to 10. The loop will request
    data until the user input is valid.
    """

    print('Please choose a number between 1 to 10.')
    number = []
    while True:
        try:
            get_num = input('Enter your number here:\n')

            player_num = int(get_num)

            if player_num > 0 and player_num < 11:
                clear()
                print(f'Your choice is {player_num}\n')
                number.append(player_num)
                break
            else:
                print('Please choose a valid number.')
                time.sleep(1.0)
                continue
        except ValueError:
            print('Not a number: please try again.\n')
            time.sleep(1.0)
            continue
    time.sleep(1.0)
    get_color_list(player_num, lives)


def get_color_list(player_num, lives):
    """
    Get a list of colors displayed in terminal.
    Check if number input value is an even or odd number,
    print differnet list depending on number.
    """
    print('Choose a color:')

    if player_num % 2 == 0:
        for color in color_list_one:
            print(color, end=' ')
        time.sleep(1.0)
        get_color(color_list_one, lives)
    else:
        for color in color_list_two:
            print(color, end=' ')
        time.sleep(1.0)
        get_color(color_list_two, lives)


def get_color(color_list, lives):
    """
    Get a color input from the player.
    Checks if the input value matches with options,
    if input is valid, runs a math function.
    """
    while True:
        try:
            player_color = input('\n\nEnter your color choice:\n')
            if player_color in color_list:
                for index, color in enumerate(color_list):
                    if color == player_color:
                        clear()
                        print(f'Your choice is {player_color}.\n')
                        math_quest(index, lives)
                        break
                break
            else:
                print(f'{player_color} is not a valid color, try again.\n')
                continue
        except ValueError:
            print(f'{player_color} is not a valid color, please try again.\n')
            continue


def math_quest(index, lives):
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
    get_answer(answer, lives)


def get_answer(answer, lives):
    """
    Let player submit answer.
    The input value has to be an integer.
    Check if answer provided is correct or incorrect.
    """
    while True:
        try:
            player_answer = int(input('Enter your answer here: '))
            clear()
            if player_answer != answer:
                lives -= 1
                if lives == 0:
                    print(f'You got this one wrong! Its {answer}\n')
                    time.sleep(0.75)
                    print('But wait...\n')
                    time.sleep(1.0)
                    print('Oh no! You are out of lives!\n')
                    time.sleep(1.5)
                    play_again(3)
                print(f'Oh no, you got this one wrong! Its {answer}\n')
                if lives == 1:
                    print(f'You have {lives} life remaining\n')
                else:
                    print(f'You have {lives} lives remaining\n')
                time.sleep(1.0)
                get_player_num(lives)
                break
            else:
                print(f'Hooray! {answer} is the right answer\n')
                if lives == 1:
                    print(f'You have {lives} life remaining\n')
                else:
                    print(f'You have {lives} lives remaining\n')
                time.sleep(1.0)
                get_player_num(lives)
                break
        except ValueError:
            print('Not a number: please try again.\n')
            time.sleep(1.0)
            continue


def play_again(lives):
    """
    Give the player an option to choose through input
    if they want to play again or leav the game.
    """

    while True:
        print('Would you like to play again? y = yes, n = no')
        game = input('Enter y or n: \n')

        if game.lower() == 'y':
            print("\nGreat, let's play again")
            time.sleep(1.5)
            clear()
            get_player_num(lives)
            break
        elif game.lower() == 'n':
            print('\nNow leaving the game...\n')
            print('Thank you for playing Loppan!')
            time.sleep(2.5)
            main()
        else:
            print(f'{game} is not a valid option')

    clear()


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
    clear()
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
    The game originates from Japan. The earliest record of using the Loppa in
    the western world is from 1836. If you would like to know more,
    you can visit these websites:

    http://www.origamiheaven.com/historyofthesaltcellar.htm
    https://en.wikipedia.org/wiki/Paper_fortune_teller
    """)


def create_own():
    """
    Will print information about how the user can make their own 'Loppa'
    """
    clear()
    print("""
    Create Your Own
    To make a Loppa/fortune teller, you need:
        * a piece of A4 paper or a squared shape paper
        * scissor
        * pencils""")

    input('\nPress Enter to proceed')

    print("""
    Instructions:
    1. Fold the corners of a sheet of paper so they meet up
        on the opposite sides.
        If the paper is not a square, cut the top off,
        making it a square sheet with diagonal creases.""")

    input('\nPress Enter to proceed')

    print("""
    2. Fold the four corners of the square into the center,
        forming a shape known in origami terminology as a
        blintz base or cushion fold.
        Turn the paper square over,
        and fold the four corners into the middle a second time.""")

    input('\nPress Enter to proceed')

    print("""
    3. The top of the square should look like a squared cake with 8 slices.
        On each slice, you can put a number or a color.
        Open up one of the corners at a time and write a fortune
        or a task under each slice.""")

    input('\nPress Enter to proceed')

    print("""
    4. When done, it should look like a folded cushion,
        as at the end of step 2.
        Work your fingers into the pockets on the backside of the cushion,
        all the way into the four corners.
    """)


def exit_game():
    """
    The user will exit the game
    """
    clear()
    # print('Exit Game \n')


def main():
    """
    The main function of the program with the start menu
    for the user to navigate through the program.
    """
    clear()
    while True:
        print('Welcome to the game of "Loppan".\n')
        print_menu()
        option = ''
        try:
            option = int(input('\nWhere do you want to go? Enter number:\n'))
        except ValueError as e:
            print(f'Invalid data: {e}, try again.\n')

        clear()
        if option == 1:
            about_game()
        elif option == 2:
            clear()
            print("""
The game of Loppan will test your mathematical skills.
You get 3 lives during the game, and if you answer a question incorrectly,
you lose 1 life.
Follow the instruction provided. """)
            print("\nLet's start!\n")
            get_player_num(lives)
        elif option == 3:
            create_own()
        elif option == 0:
            exit_game()
            break
        else:
            print('Not a valid input.')
            print('Please chose a number between 0 and 3\n')

    print('Thank you for visiting "Loppan". Please come back again')
    sys.exit()


if __name__ == '__main__':
    main()

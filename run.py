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
                    print(f'Your choice is {player_color}\n')
                    math_quest(index)
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
        print(f'Hooray! {answer} is the right answer')
    else:
        print(f'Oh no, you got this one wrong! Its {answer}')


def go_game():
    get_player_num()
    # math_quest(index)


go_game()

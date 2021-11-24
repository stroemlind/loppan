# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Lists for the game functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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

    print(number)


get_player_num()

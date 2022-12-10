import random

"""
Define a subroutine that prompts the user for a number and stores it in the num variable.
Define another routine that uses the value of num and counts from 1 to that number.
"""

# def get_num():
#     num = int(input('Enter num: '))
#     return num
#
#
# def main():
#     num = get_num()
#     for i in range(1, num + 1):
#         print(i)
#
#
# main()


"""
Define a subroutine which prompts the user to select a large
and a small number, and then generates a random number
from this range and stores it in a variable called comp_num.
Define another subroutine that outputs
the message “I am thinking of a number…”, after which it prompts the user to guess
hidden number. Define a third routine that checks if
does comp_num match with the user's guess. If it matches, then
the subroutine displays the message "Correct, you win";
otherwise loop continues, and the subroutine tells whether more or
less their guess hidden number, and offers to make a new attempt
until the user guesses it.
"""


def com_nums():
    low = int(input('Enter low num: '))
    height = int(input('Enter height num: '))
    comp_num = random.randint(low, height)
    return comp_num


def comp_guess():
    print('I am thinking of a number…')
    userNum = int(input('Guess number: '))
    return userNum


def main():
    com_num = com_nums()
    while True:
        userNum = comp_guess()
        if userNum < com_num:
            print('large')
        elif userNum > com_num:
            print('lower')
        elif userNum == com_num:
            break
        else:
            print('Please try again')

    print('Correct, you win')


if __name__ == '__main__':
    main()

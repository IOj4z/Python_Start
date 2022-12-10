import csv
import random
from re import match

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

#
# def com_nums():
#     low = int(input('Enter low num: '))
#     height = int(input('Enter height num: '))
#     comp_num = random.randint(low, height)
#     return comp_num
#
#
# def comp_guess():
#     print('I am thinking of a number…')
#     userNum = int(input('Guess number: '))
#     return userNum
#
#
# def main():
#     com_num = com_nums()
#     while True:
#         userNum = comp_guess()
#         if userNum < com_num:
#             print('large')
#         elif userNum > com_num:
#             print('lower')
#         elif userNum == com_num:
#             break
#         else:
#             print('Please try again')
#
#     print('Correct, you win')
#
#
# if __name__ == '__main__':
#     main()


"""
Write a program that helps the user easily manage a list of names. 
Program should display a menu that allows you to add, change and remove names from the list, and display them all. 
In addition, there must be a command in the menu to complete program work. 
If the user has selected a non-existent command, the program displays an appropriate message. 
After the user selects the command to add, change, or deleting a name or viewing all names, 
the menu should be displayed again without having to restart the program. 
The program should be as simple and easy to use as possible.
"""


def add_name():
    name = input('Enter name: ')
    names.append(name)
    return names


def change_name():
    x = 0
    for i in names:
        print(f"{x}) {i}")
        x = x + 1

    editName = int(input('Enter num for edit: '))
    names[editName] = input('Enter new name : ')
    return names


def remove_name():
    x = 0
    for i in names:
        print(f"{x}) {i}")
        x = x + 1
    deletName = int(input('Enter num for delete: '))
    del names[deletName]
    return names


def display_names():
    for i in names:
        print(i)
    print()


def done_program():
    print('Good bye!')
    return True


def main():
    command = ('Add_name', 'Edit name', 'Remove name', 'Display list', 'Exit program')
    x = 1
    while True:
        for c in command:
            if x > 5:
                x = 1
            print(f"{x}) {c}")
            x = x + 1
        userCommand = int(input('Choose command num: '))
        match (userCommand):
            case 1:
                names = add_name()
            case 2:
                names = change_name()
            case 3:
                names = remove_name()
            case 4:
                names = display_names()
            case 5:
                if done_program():
                    break
            case _:
                print("Incorrect option: ")


names = []

if __name__ == '__main__':
    main()

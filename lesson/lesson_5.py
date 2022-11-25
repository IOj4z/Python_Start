"""
Prompt the user to enter a name.
Bring out name three times.
"""
# name = input("Enter your name: ")
#
# for i in range(1, 4):
#     print(name)
#

"""
Modify the program from Exercise 35 so that it asks
user to enter a name and a number, and then output the name given
number of times.
"""
# name = input("Enter your name: ")
# num = int(input("Enter num: "))
#
# for i in range(1, num + 1):
#     print(name)

"""
Prompt the user to enter a name. 
Print each letter of the name
on a separate line.
"""
# name = input("Enter your name: ")
# num = int(input("Enter num: "))
# for i in range(1, num + 1):
#     for x in name:
#         print(x)


"""
Prompt the user to enter a number from 1 up to 12. 
Print the multiplication table for this numbers.
"""

# num = int(input("Enter a number from 1 up to 12: "))
# for i in range(1, 10):
#     print(f"{num} * {i} = {num * i}")

"""
Prompt the user to enter a number up to 50.
Reverse countdown from 50 to the entered number.
Make sure that the entered number is included in the output.
"""

# num = int(input("Enter a number from 1 to 50: "))
#
# for i in range(51, num - 1, -1):
#     print(i)


"""
Prompt the user to enter a name and a number.
If the number is less than 10,
the program should display the name a specified number of times; 
otherwise it outputs "Too high" message three times.
"""

# name = input("Enter your name: ")
# num = int(input("Enter num: "))
#
# if num < 10:
#     for i in range(1, num + 1):
#         print(name)
#
# else:
#     for i in range(1, 4):
#         print("Too high")


"""
Set the variable named total to 0. 
Suggest the user to enter five numbers, and after each entry ask if he wants to include this number in the summation. 
If the answer is positive, add the entered number to total. 
If the answer will be negative, the number is not added to total. 
After entering all five numbers print the value of total.
"""

# total = 0
# for i in range(6, 1, -1):
#     num = int(input("Enter num: "))
#     if input('include this number in summation? "yes|no": ') == 'yes':
#         total += num
#
# print(total)

"""
Ask the user in which direction they want to count (forward or backward). 
If a direct count is selected, ask for a number and count from 1 to the entered number. 
If selected countdown, request a number less than 20, and then count down from 20 to the given number. 
If something else is entered, print the message "I don't understand".
"""

# way = input('which direction they want to count? "forward | backward": ')
# if way == 'forward':
#     num = int(input("Enter num: "))
#     for i in range(1, num + 1):
#         print(i)
# elif way == 'backward':
#     num = int(input("Enter num less 20: "))
#     for i in range(20, num - 1, -1):
#         print(i)
#
# else:
#     print('I don’t understand')

"""
Ask the user how many people they want to invite to the party. 
If it is entered number less than 10, ask for names and after each name print the string "[name] has been invited".
If the number entered is greater than or equal to 10, display the message "Too many people".
"""
guest = int(input("How many people would you like to invite to the party? "))
if guest < 10:
    for i in range(1, guest + 1):
        name = input(f"Enter {i} name: ")
        print(f"{name} has been invited")

elif guest >= 10:
    print("Too many people")


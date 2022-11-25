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

name = input("Enter your name: ")
num = int(input("Enter num: "))

if num < 10:
    for i in range(1, num + 1):
        print(name)

else:
    for i in range(1, 4):
        print("Too high")
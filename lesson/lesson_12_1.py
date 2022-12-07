import random
"""
Create a new file named numbers.txt.
Add five to it numbers that are stored on the same line and separated only commas.
After starting the program, find folder where your program; make sure that file has been created.
On a Windows system to view the contents of the new text file easiest to use "Notepad".
"""

# file = open('file/Numbers.txt', 'w')
# for i in range(5, 1, -1):
#     nums = random.randint(1, 1000)
#     string = str(nums)
#     file.write(string + ', ')
#
# file.close()
# file = open('file/Numbers.txt', 'r')
# print(file.read())

"""
Create a new file named Names.txt. 
Add five names to it, displayed on different lines. 
After starting the program, find the folder where your program is located; 
make sure the file was created.
"""

# file = open('Names.txt', 'w')
# file.write('Alex\n')
# file.write('John\n')
# file.write('Jerry\n')
# file.write('Francis\n')
# file.write('Felix\n')
# file.close()

"""
Open file Names.txt and output the data
from code Python.
"""

# file = open('Names.txt', 'r')
# print(file.read())


"""
Open the Names.txt file. 
Prompt the user to enter a new name. 
Add it to the end of the file and output everything
file contents.
"""

# userName = input('Enter any name: ')
# file = open('Names.txt', 'a')
# file.write(userName)
# file.close()
#
# file = open('Names.txt', 'r')
# print(file.read())
# file.close()

"""
Bring up the following menu:
1) Create a new file
2) Display the file
3) Add a new item to the file
Make a selection 1, 2 or 3:
Ask the user to select one of the options.
If the user enters anything other than 1, 2, and 3, 
the program should display an appropriate message about error.
If the user selects 1, prompt him to enter the name of the school subject and save it in a new file
named Subject.txt. An existing file with the same name
must be replaced with a new file.
If the user selects 2, the contents of the Subject.txt file are displayed.
If the user selects 3, prompt the user
enter a new item, save it to a file, and then output all its contents.
Run the program several times to test different teams.
"""


# while True:
#     userInput = int(
#         input('1) Create a new file  2) Display the file  3) Add a new item to the file Make a selection 1, '
#               '2 or 3: '))
#     if userInput == 1:
#         subject = input('Enter name of the school subject: ')
#         file = open('Subject.txt', 'w')
#         file.write(subject + '\n')
#         file.close()
#         break
#     elif userInput == 2:
#         file = open('Subject.txt', 'r')
#         print(file.read())
#         file.close()
#         break
#     elif userInput == 3:
#         subject = input('Enter new name of the school subject: ')
#         file = open('Subject.txt', 'a')
#         file.write(subject + '\n')
#         file.close()
#         file = open('Subject.txt', 'r')
#         print(file.read())
#         file.close()
#         break
#     else:
#         print('Please enter correct num: 1 | 2 | 3')


"""
With the help of the previously created file Names.txt list names in python. 
Ask user enter one of the names and then save all,
except for the selected in a new file, under Names2.txt.
"""
file = open('Names.txt', 'r')
print(file.read())
file.close()

file = open('Names.txt', 'r')
userName = input('Enter name: ') + '\n'
for n in file:
    if userName != n:
        nfile = open('Names2.txt', 'a')
        nfile.write(n)
        nfile.close()

file.close()
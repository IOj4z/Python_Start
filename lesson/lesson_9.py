"""
Offer the user enter your name and then print the length of the name.
Ask for the last name and print the length of the last name.
Connect the first name with the last name, separating them with a space, and output the result.
Finally, print the length of the full name (including spaces).
"""

# userFirstName = input('Enter First name: ')
# print(len(userFirstName))
# userLastName = input('Enter Last name: ')
# print(len(userLastName))
# print(userFirstName, userLastName, sep=" ")
# print(len(userFirstName + " " + userLastName))

"""
Ask the user to enter their favorite school subject.
Print it in such a way that each letter is followed by a hyphen — e.g. S-p-a-n-i-s-h-.
"""

#
# subject = input('Enter lovely subject: ')
# for i in subject:
#     print(i, end='-')
"""
Draw a line from your favorite poem and suggest the user to enter a start and end position. 
Bring out characters in between.
"""
# favorite = input('Enter line from your favorite poem: ')
# x = int(input('Enter start pos. number: '))
# y = int(input('Enter end pos. number: '))
# print(favorite[x:y])

"""
Prompt the user to enter a word in upper case. 
If a not all letters of the word will be in upper case, please ask re-enter the word. 
Retry until the user will enter the message in upper case.
"""

# while not input('Enter word in upper case: ').isupper():
#     continue


"""
Prompt the user to enter a name,
and then tell how many vowels it has letters.
"""
# name = input('Enter name: ')
# count = 0
# name = name.lower()
# for x in name:
#     if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#         count = count + 1
#
# print("Vowels = ", count)


"""
Prompt the user for a password, and then offer to enter it again. 
If the two passwords match, print the message "Thank you". 
If letters entered correctly, but differ in case, display the message "They must be in the same case";
otherwise, the message "Incorrect" is displayed.
"""

pas = input('Enter password: ')
confPas = input('Confirm password: ')
if pas == confPas:
    print('Thank you')
elif pas.lower() == confPas.lower():
    print('They must be in the same case')
else:
    print('Incorrect')

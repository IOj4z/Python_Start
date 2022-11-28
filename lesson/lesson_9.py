
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
favorite = input('Enter line from your favorite poem: ')
x = int(input('Enter start pos. number: '))
y = int(input('Enter end pos. number: '))
print(favorite[x:y])
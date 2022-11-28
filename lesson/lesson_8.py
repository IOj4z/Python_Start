"""
Create a tuple with the names of the five countries. 
Output the entire contents of the tuple. 
Suggest the user to enter the name of one of these 
countries and output the index (that is, the position in the list)
this element of the tuple.
"""

# countryName = ('Paris', 'England', 'Japan', 'South-Korea', 'North-Korea')
# print(countryName)
# userChoose = input('Choose country: ')
# if userChoose in countryName:
#     print(countryName.index(userChoose))


"""
prompted the user enter a number and display the name
country located in a given positions.
"""

# countryName = ('Paris', 'England', 'Japan', 'South-Korea', 'North-Korea')
# userChoose = int(input('Enter number: '))
# print(countryName[userChoose])

"""
Create a list with names of two kinds sports. 
Prompt the user to enter your favorite sport and add it
to the end of the list. Sort the list and output it.
"""
#
# sportType = ['Box', 'Football', input("Enter lovely sport type: ")]
# sportType.sort()
# print(sportType)

"""
Create a list with the names of six school subjects. 
Ask the user which of these items they don't like. 
Remove selected items from list and print it again.
"""

# schoolSubject = ['Mathematics', 'Science', 'Health', 'Art', 'Movement or Eurythmy']
# print(schoolSubject)
#
# while True:
#     userChoise = input(f'Which of these subjects doesnt like you: ')
#     schoolSubject.remove(userChoise)
#     print(schoolSubject)
#     if input(f'One more? "yes | no"') == 'no':
#         break

"""
Prompt the user to enter names of four
favorite dishes and save them in a layer var with numeric
indexes, starting c 1. Print the contents of the dictionary
with indication of indexes and elements.
Ask the user which element he wants to exclude
and remove it from list. Sort the rest data and output
dictionary content.
"""
# userEnter = []
# for i in range(4, 0, -1):
#     favoriteDish = input(f'Enter favorite dish {i}: ')
#     userEnter.insert(i, favoriteDish)
#
#
# for item in userEnter:
#     print(f"{userEnter.index(item) + 1}: {item}")
#
#
# doesntLike = input('Which one want delete from list: ')
# userEnter.remove(doesntLike)
# userEnter.sort()
#
# for item in userEnter:
#     print(f"{userEnter.index(item) + 1}: {item}")

"""
Ask the user to enter the names of the three people they want
invite to a party, and save them to a list. 
After they will all three numbers are entered, ask if the user wants to add more one name. 
If the answer is yes, invite him to add names until you get a "no" response. 
After answering "no" print the number of people invited to the party
"""
# invitedGuest = []
# for i in range(4, 1, -1):
#     invitedGuest.append(input("Enter name to invite: "))
#
# while input("Want invite more 'yes|no': ") == 'yes':
#     invitedGuest.append(input("Enter name to invite: "))
#
# print(f"{len(invitedGuest)} was invited person to the party.")

"""
Modify Program 076 so that after entering the list of names, the program will output the complete list.
Prompt the user to enter one of the names in the list and output the position of the name in the list. 
Ask-See if the user wants this person to attend the party. 
If the user answers "no", remove the item from the list and print the list again.
"""

invitedGuest = []
for i in range(4, 1, -1):
    invitedGuest.append(input("Enter name to invite: "))
while input("Want invite more 'yes|no': ") == 'yes':
    invitedGuest.append(input("Enter one more name to invite: "))
    if input("Want invite more 'yes|no': ") == 'yes':
        break
print(f"{len(invitedGuest)} was invited person to the party.")
doesntWant = input('Enter one of the names in the list: ')
print(f"{invitedGuest.index(doesntWant) + 1}: {doesntWant}")

if input('Should this person to attend the party? "yes|no"') == 'no':
    invitedGuest.remove(doesntWant)

for person in invitedGuest:
    print(f"{invitedGuest.index(person) + 1}: {person}")

"""

"""

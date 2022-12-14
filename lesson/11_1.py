"""
Create the following dataset
as a simple two-dimensional list
with standard Python indexes:
"""
nums = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

"""
prompt the user to select a row and column and output the selected value.
"""
# print(nums)
# userRow = int(input("Enter row index: "))
# userColumn = int(input("Enter column index: "))
# print(nums[userRow][userColumn])

"""
prompt the user to select a row and output only her. 
Prompt to enter a new value, add it to the end of the line, 
then output again changed line.
"""

# userRow = int(input("Enter row index: "))
# print(nums[userRow])
# userNewVal = int(input("Enter value: "))
# nums[userRow].append(userNewVal)
# print(nums[userRow])

"""
Ask the user to select a string and display only that string. 
Offer to select a column from the displayed row and print only the value stored there.
Ask if the user wants to change his. 
If the answer is yes, prompt to enter a new value and change the data. 
Finally output again changed line.
"""
# userRow = int(input("Enter row index: "))
# print(nums[userRow])
# userColumn = int(input("Enter column index: "))
# print(nums[userRow][userColumn])
# if input('Do you want change? "yes|no": ') == 'yes':
#     userNewVal = int(input("Enter value: "))
#     nums[userRow][userColumn] = userNewVal
#     print(nums[userRow][userColumn])
#
# print(nums[userRow])

"""
Create the following dataset representing sales volumes by region, 
in the form of a two-dimensional dictionary:
"""
data = {
    'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
    'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
    'Anna': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
    'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451},
}

"""
prompt the user for a name and region. 
Output the relevant data. 
Prompt the user for the name and region of the value they want to change, 
and let them adjust the sales volume. 
Display the sales volumes for all regions for
the name chosen by the user.
"""

# userName = input("Enter name: ")
# region = input("Enter region: ").upper()
# print(data[userName][region[0]])

"""
Ask the user to enter the name, age, and shoe size for four people. 
Ask for the name of one of them in the list 
and print the values for his age and shoe size.
"""
# data_set = {}
# for data in range(4, 0, -1):
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     shoeSize = input("Enter shoeSize: ")
#     data_set[name] = {'age': age, 'shoes': shoeSize}
#
#
# chooseData = input("Enter name to get info: ")
# print(data_set[chooseData])


"""
so that it displays the name and age for
all the people on the list, but is not their shoe size.
"""
#
# data_set = {}
# for data in range(1, 0, -1):
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     shoeSize = input("Enter shoeSize: ")
#     data_set[name] = {'age': age, 'shoes': shoeSize}
#
# for name in data_set:
#     print((name), data_set[name]['age'])

"""
After receiving the name, age and shoe size for four people
prompt the user for the name of the person to be removed from the list. Delete
this line and output the rest of the data broken down by lines.
"""
data_set = {}
for data in range(4, 0, -1):
    name = input("Enter name: ")
    age = input("Enter age: ")
    shoeSize = input("Enter shoeSize: ")
    data_set[name] = {'age': age, 'shoes': shoeSize}

delete = input("Enter name to remove from the data? ")
del data_set[delete]
for name in data_set:
    print((name), data_set[name]['age'])

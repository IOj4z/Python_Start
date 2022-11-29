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
userRow = int(input("Enter row index: "))
print(nums[userRow])
userColumn = int(input("Enter column index: "))
print(nums[userRow][userColumn])
if input('Do you want change? "yes|no": ') == 'yes':
    userNewVal = int(input("Enter value: "))
    nums[userRow][userColumn] = userNewVal
    print(nums[userRow][userColumn])

print(nums[userRow])

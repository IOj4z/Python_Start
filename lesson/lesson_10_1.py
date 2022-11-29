import random
from array import *

"""
Prompt the user to enter whole numbers.
If the user enters a number between 10 and 20, store it in an array;
otherwise, print the message "Outside the range".
After five numbers have been successfully added to the array,
print the message "Thank you" and output an array, each
whose element would be on a separate line.
"""

# nums = array('i', [])
# while len(nums) != 5:
#     nums.append(int(input("Enter num: ")))
#
# nums = sorted(nums)
# nums.reverse()
# print(nums)

"""
Create an array to store integers. 
Generate five random numbers and store them in an array.
Output the array (each element must be displayed on a separate line).
"""
# integers = array('i', [])
#
# for i in range(5, 0, -1):
#     integers.append(random.randint(1, 10000))
#
# for x in integers:
#     print(x)

"""
Prompt the user to enter whole numbers. 
If the user enters a number between 10 and 20, 
store it in an array; otherwise, print the message "Outside the range".
After five numbers have been successfully added to the array,
print the message "Thank you" and output an array, each
whose element would be on a separate line.
"""
userNum = array('i', [])
count = 0
while count != 5:
    userEnter = int(input('Enter number: '))
    if 10 >= userEnter <= 20:
        userNum.append(userEnter)
        count += 1
    else:
        print('Outside the range')
print('Thank you')
for i in userNum:
    print(i)

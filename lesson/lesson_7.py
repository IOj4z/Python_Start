import random

"""
Output a random number in the range
from 1 to 100 inclusive.
"""
#
# num = random.randint(1, 100)
# print(num)

"""
Get a random name fruit from the list
containing five titles.
"""
# fruit = ['apple', 'orange', 'blueberry', 'banana', 'strawberry']
# print(random.choice(fruit))

"""
Randomly choose heads or tails ("h" or "t"). 
Ask the user to guess your choice. 
If a your choice matches a randomly chosen value, display the message "You win"; 
otherwise, print the message "Bad luck". 
At the end, tell the user what value was guessed - “heads” or “tails”.
"""
# side = random.choice(['heads', 'tails'])
# userChoise = input("Guess my choice? 'heads | tails': ")
# if userChoise == side:
#     print("You win")
# else:
#     print("Bad luck")
# print(side)

"""
Pick a random number between 1 and 5. 
Ask the user to pick a number. If he guessed right, print the message "Well done"; 
otherwise report that his number is greater or less than yours, and offer to choose another number. 
If the user guessed right the second time, display the message "Correct",
and if not, the message "You lose".
"""
num = random.randint(1, 100)

count = 0
while True:
    if count >= 7:
        print('Your lose')
        break
    userNum = int(input("Guess number: "))
    count += 1
    if userNum == num and count >= 2:
        print("Correct")
        break
    elif userNum == num:
        print("Well done")
        break
    elif userNum > num:
        print("High")
    elif userNum < num:
        print("Low")






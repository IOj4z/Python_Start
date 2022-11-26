
"""
Set total to 0. While total is 50 or less, prompt the user to enter a number.
Add this number to total and print the message "The total is… [total]".
The loop should stop when the value of total will exceed 50.
"""
# total = 0
# while total <= 50:
#     num = int(input("Enter a number: "))
#     total = total + num
# print("The total is ", total)


"""
Prompt the user to enter a number. 
Keep asking for a number until the entered
the number will not be greater than 5, after
then display the message "The last number you entered was a
[number]" and stop the program.
"""
# num = 0
# while num < 5:
#     num = int(input("Enter a number: "))
# print(f"The last number you entered was a {num}")


"""
Ask the user to enter first one number and then another. 
Add two numbers and ask if he wants to add one more. 
If he enters "y", offer to enter one more number; 
it goes on until until the user enters the answer is "y". 
After the cycle stops, print the amount.
"""

# a = int(input("Enter number A:"))
# b = int(input("Enter number B:"))
# total = a + b
# while input("Add one more? 'y|n'") == 'y':
#     c = int(input("Enter number C:"))
#     total += c
# print("Total ", total)

"""
Prompt the user to enter the name of the person
the user wants to invite to a party. 
After that, print the message "[name] has been invited" and increment the counter by 1. 
Ask if the user wants to invite someone more. 
Keep prompting for names until the user will answer in the negative, 
and print the number of invitees.
"""
# count = 0
#
# while True:
#     person = input("Enter name to Invite person: ")
#     count = count + 1
#     print(f"{person} has been invited")
#     if input("Invite one more? 'y|n'") == 'y':
#         continue
#     else:
#         break
# print(f"{count} guest was invited")

"""
Create a variable called compnum and assign it value 50. 
Prompt the user to enter a number. 
Bye guess does not match with compnum value, 
tell if it is greater or less compnum and prompt to enter another number. 
If the entered value will match compnum,
print the message "Well done, you took [attempts] attempts".
"""
# compnum = 50
# userNum = int(input("Enter number: "))
# count = 1
#
# while userNum != compnum:
#     if userNum > compnum:
#         print("Enter num is high")
#         userNum = int(input("Enter over number: "))
#         count += 1
#     elif userNum < compnum:
#         print("Enter num is lower")
#         userNum = int(input("Enter over number: "))
#         count += 1
#
# print(f"«Well done, you took {count} attempts")

"""
Prompt the user to enter number from 10 to 20. 
If the entered value is less than 10, display the message "Too low" and prompt to retry. 
If the entered value is greater than 20, display the message "Too high" and prompt to retry. 
repeat until it is entered value from the range from 10 to 20, then display a message Thank you.
"""

# userNum = 0
#
# while userNum < 10 or userNum > 20:
#     userNum = int(input("Enter number from 10 to 20: "))
#     if userNum < 10:
#         print("Too low")
#     elif userNum > 20:
#         print("Too high")
# print("Thank you")

"""
Print the lines "There are [counter] green bottles hanging on the wall, [counter] green bottles hanging on the wall, 
and if 1 green bottle should accidentally fall". 
Then print the question: "how many green bottles will be hanging on the wall?”. 
If the user answers correctly, display the message "There will be [counter] green bottles hanging on the wall". 
If the user answers incorrectly, display the message "No, try again" until the correct answer is given. 
When the counter goes down to 0, print the message "There are no more green bottles hanging on the wall".
"""
num = 10
while num > 0:
    print("There are ", num, " green bottles hanging on the wall.")
    print(num, " green bottles hanging on the wall.")
    print("And if 1 green bottle should accidentally fall,")
    num = num - 1
    answer = int(input("How many green bottles will be hanging on the wall? "))
    if answer == num:
        print("There will be ", num, " green bottles hanging on the wall.")
    else:
        while answer != num:
            answer = int(input("No, try again: "))
            print("There are no more green bottles hanging on the wall.")
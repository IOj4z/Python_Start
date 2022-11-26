
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
count = 0

while True:
    person = input("Enter name to Invite person: ")
    count = count + 1
    print(f"{person} has been invited")
    if input("Invite one more? 'y|n'") == 'y':
        continue
    else:
        break
print(f"{count} guest was invited")
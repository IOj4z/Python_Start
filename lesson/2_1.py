"""
Offer the user enter two numbers.
If the first number is greater than the second one,
print the second number first,
and then the first.
Otherwise If so, output the first
first number, and then the second.
"""

# firstNum = int(input("Enter first number: "))
# secondNum = int(input("Enter second number: "))
#
# if  firstNum > secondNum:
#     print(f"SecNumber {secondNum}, FirsNum {firstNum}")
# else:
#     print(f"FirsNum {firstNum}, SecNumber {secondNum}")

"""
   Prompt the user to enter a number less than 20. 
   If the entered number greater than or equal to 20, 
   display the message "Too high"; otherwise, 
   print the message "Thank you".
"""
# lessNum = int(input("Enter number less than 20: "))
# if lessNum >= 20:
#     print("Too high")
# else:
#     print("Thank you")

"""
 Offer the user enter a number from 10 to 20 (inclusive). 
 If it is entered a number from this range, 
 display the message "Thank you";
 otherwise, output "Incorrect answer" message.
"""
# num = int(input("Enter number from 10 to 20: "))
# if 10 <= num <= 20:
#     print("Thank you")
# else:
#     print("Incorrect answer")

"""
Prompt the user to enter a favorite color. 
If he types "red", "RED" or "Red", 
display the message "I like red too". 
Otherwise, print the message 
"I don't like [colour], I prefer red".
"""
# color = input("Enter lovely color: ")
#
# if color.lower() == 'red':
#     print("I like red too")
# else:
#     print(f"I don't like {color}, I prefer red")


"""
Ask the user if it's raining. Convert his answer to lowercase
str. If the user answers yes, ask if it's windy outside. If the user
The caller will answer "yes" and for the second question, print the message "It is too windy
for an umbrella"; otherwise, print the message "Take an umbrella".
If the user did not give a positive answer to the first question, 
display the message "Enjoy your day".
"""

# if input('Is it raining? "yes|no": ') == 'yes':
#     if input('Is it windy outside? "yes|no": ') == 'yes':
#         print("It is too windy for an umbrella")
#     else:
#         print("Take an umbrella")
# else:
#     print("Enjoy your day")


"""
Offer the user enter his age. 
If a the entered value is 18 or more, 
display the message "You can vote"; 
if 17 - message "You can learn to drive"; 
if 16 - the message "You can buy a lottery ticket. 
If the value less than 16, print the message 
"You can go Trickor-Treatment.
"""
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote")
# elif age == 17:
#     print("You can learn to drive")
# elif age == 16:
#     print("You can buy a lottery ticket")
# elif age < 16:
#     print("You can go Trickor-Treating")


# userNum = int(input("Enter number: "))
#
# if userNum < 10:
#     print("Too low")
# elif 10 <= userNum <= 20:
#     print("Correct")
# else:
#     print("Too high")
"""
Prompt the user to enter a value of 1, 2, or 3. If the value is 1, 
display the message "Thank you"; if 2 - message "Well done"; 
if 3 - the message "Correct". If entered
any other value, print the message "Error message".
"""
userVal = int(input("Enter val 1,2 or 3: "))
if userVal == 1:
    print("Thank you")
elif userVal == 2:
    print("Well done")
elif userVal == 3:
    print("Correct")
else:
    print("Error message")
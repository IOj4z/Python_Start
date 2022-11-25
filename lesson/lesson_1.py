"""
Ask the user to enter their name
and display a welcome message.
Hello [name].

"""

# name = input("Whats your name? ")
#
# print("Hello", name)


"""
Ask the user to enter their first and last name
and then display a welcome message.
Hello [first name] [last name].

"""


# firstName = input("Whats your First name? ")
# lastName = input("Whats your Last name? ")
#
# print("Hello", firstName, lastName)

"""
Write code that prints the question "What do you call a bear with no teeth?",
and on the next line prints the answer: "A gummy bear!" Try to get by
with one line of code.

"""
# print("What do you call a bear with no teeth?\nA gummy bear!")


"""
Offer the user
enter two numbers. Fold up
these numbers and print the result in the form
The total is [result].
"""

# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))
#
# c = a + b
#
# print(f"The total is {c}")

"""
Offer the user enter three numbers. 
Fold up first two numbers, then multiply the amount on the third number. 
Output the result as The answer is [result].
"""
# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))
# c = int(input("Enter number c: "))
#
# e = (a + b) * c
#
# print(f"The answer is {e}")

"""
Ask how many slices of pizza the user had and 
how much he ate the pieces. 
Calculate how many slices of pizza he has left, 
and print the result in the form
"""
# a = int(input("How much was: "))
# b = int(input("How much ate: "))
# # c = int(input("How much is left: "))
#
# e = a - b
# print(f"How much is left: {e}")
#

"""
Prompt the user to enter their name and age. Increase the age by 1 and display the message:
[name] next birthday you will be [new age].
"""
# firstName = input("Whats your First name? ")
# age = int(input("How old are you? "))
#
# print(f"{firstName} next birthday you will be {age + 1}.")


"""
Prompt the user to enter the total amount of the invoice, and then request the total
the number of participants in the dinner. Divide the invoice amount by the number of participants
and output the amount each participant has to pay.
"""

# a = int(input("Enter the total amount of the invoice: "))
# b = int(input("Number of dinner participants: "))
# e = a / b
# print(f"every member should pay: {e}")


"""
Write a program that prompts you to enter a period of time in days.
and then displays the number of hours, minutes and seconds in this interval.
"""
days = int(input("Enter the number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("In ", days, " days there are...")
print(hours, " hours")
print(minutes, " minutes")
print(seconds, " seconds")


"""
There are 2.204 pounds in one kilogram. Prompt the user to enter a weight in kilograms and convert it to pounds.
"""
# pounds_inequality = 2.204
# kg_inequality = int(input("Enter weight in kilograms: "))
# e = pounds_inequality * kg_inequality
# print(f"weight in pounds: {e}")

"""
Prompt the user to enter a number greater than 100 and then a number less than 10. Tell the number of times the smaller 
number fits into the larger one, in a convenient format.
"""
# a = int(input("Enter number greater than 100: "))
# b = int(input("Enter number less than 10: "))
# e = a / b
# print(f"{int(e)} times the smaller number fits in the larger")
import math


"""
Prompt the user to enter a number
with more decimal places parts.
Multiply this number by 2 and print the answer.
"""
# num = float(input("Enter float number: "))
# print(num * 2)


"""
Modify the program from task 027 so that it
displayed the result with an accuracy of two decimal places
in the fractional part.
"""
# num = float(input("Enter float number: "))
# print(round(num * 2, 2))

"""
Prompt the user to enter an integer greater than 500. Calculate the square root of this number
and output it up to two decimal places in fractional
parts.
"""
# num = float(input("Enter float number: "))
# res = math.sqrt(num)
# print(round(res, 2))

"""
Print the number "pi" (π) up to 5 signs.
"""
# pi = math.pi
# print(round(pi, 5))

# """
# Prompt the user to enter the radius of the circle (distance from the center to the outer edge.)
# Calculate area of a circle (π * radius2).
# """
# radius = float(input("Enter the radius of the circle: "))
# pi = math.pi
# res = math.sqrt(radius)
# print(round(pi * res, 2))

"""
Prompt the user to enter a radius
and cylinder height. Calculate its volume
(circle area * height) and output it
up to three decimal places.
"""
# radius = float(input("Enter the radius of the circle: "))
# cylinderHeight = float(input("Enter the cylinder height: "))
#
# res = (math.pi * math.sqrt(radius)) * cylinderHeight
# print(round(res, 3))

"""
Prompt the user to enter two numbers. 
Use integer division to divide the first number by the second; 
calculate the remainder and output
response in a user-friendly way (for example,
if the user entered 7 and 2, output a line like
“If you divide 7 by 2, you get 3 with a remainder of 1”).
"""

# a = int(input('Enter num A: '))
# b = int(input('Enter num B: '))
# res = a // b
# print(f"if you divide {a} by {b}, you get {res} with a remainder {a % b}")


"""
Output the following message:
1) Square
2) Triangle
Enter a number:
If the user enters 1, the program prompts
the length of the side of the square and displays its area. 
If a user enters 2, program asks for length
sides and the height of the triangle drawn to this
side, after which it displays its area. 
If the user enters something else, the program should return an appropriate error message.
"""

user_num = int(input("1) Square, 2) Triangle enter number: "))
if user_num == 1:
    square = int(input("Enter side length of a square: "))
    print(round(math.sqrt(square), 2))
elif user_num == 2:
    triangleLength = int(input("Enter length of a triangle: "))
    triangleHeight = int(input("Enter height of a triangle: "))
    s = 0.5 * triangleLength * triangleHeight
    print(s)
else:
    print("Please enter number 1 or 2")



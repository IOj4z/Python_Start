import random
from tkinter import *


# def Call():
#     msg = Label(window, text='You pressed the button')
#     msg.place(x=30, y=50)
#     button['bg'] = 'blue'
#     button['fg'] = 'white'
#
#
# window = Tk()
# window.title('Window title')
# window.geometry('200x110')
# button = Button(text='Press me', command=Call)
# button.place(x=30, y=20, width=120, height=25)
# window.mainloop()


"""
Create a window that offers the user enter a name. 
When the user clicks the button, the window should display the message "Hello
[name]" with background color and font color change text area.
"""

#
# def click():
#     name = textbox1.get()
#     message = str('Hello ' + name)
#     textbox2['bg'] = 'yellow'
#     textbox2['fg'] = 'blue'
#     textbox2['text'] = message
#
#
# window = Tk()
# window.geometry("500x200")
# window.title('Show name')
# label1 = Label(text='Enter your name: ')
# label1.place(x=30, y=20)
#
# textbox1 = Entry()
# textbox1.place(x=150, y=20, width=200, height=25)
# textbox1['justify'] = 'center'
# textbox1.focus()
#
# button1 = Button(text='Press me', command=click)
# button1.place(x=30, y=50, width=120, height=25)
#
# textbox2 = Message(text='')
# textbox2.place(x=150, y=50, width=200, height=25)
# textbox2['bg'] = 'white'
# textbox2['fg'] = 'black'
#
# window.mainloop()


"""
Write a program throw simulation six-sided dice in a board game.
When the user clicks the button, a random integer should be displayed on the screen
number from 1 to 6
(inclusive).
"""


def click():
    num = random.randint(1, 6)
    textbox2['bg'] = 'white'
    textbox2['fg'] = 'black'
    textbox2['text'] = num


window = Tk()
window.geometry("500x200")
window.title('Show number')
label1 = Label(text='Drop dice: ')
label1.place(x=30, y=20)


button1 = Button(text='Press me', command=click)
button1.place(x=30, y=50, width=120, height=25)

textbox2 = Message()
textbox2.place(x=150, y=50, width=200, height=25)
textbox2['bg'] = 'white'
textbox2['fg'] = 'black'

window.mainloop()


"""
Write a program that prompts the user to enter a number.
in the text field. When the user presses the button, 
this number is added to the accumulated amount and displayed in another field. 
input can repeat as many times as you like discretion of the user, 
while input data will be added to the amount. 
The window should contain one more button that resets the accumulated amount and erases
the contents of the original field to  the user could start typing again.
"""
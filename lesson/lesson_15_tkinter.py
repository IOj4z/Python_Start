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


def click():
    name = textbox1.get()
    message = str('Hello ' + name)
    textbox2['bg'] = 'yellow'
    textbox2['fg'] = 'blue'
    textbox2['text'] = message


window = Tk()
window.geometry("500x200")
window.title('Show name')
label1 = Label(text='Enter your name: ')
label1.place(x=30, y=20)

textbox1 = Entry()
textbox1.place(x=150, y=20, width=200, height=25)
textbox1['justify'] = 'center'
textbox1.focus()

button1 = Button(text='Press me', command=click)
button1.place(x=30, y=50, width=120, height=25)

textbox2 = Message(text='')
textbox2.place(x=150, y=50, width=200, height=25)
textbox2['bg'] = 'white'
textbox2['fg'] = 'black'

window.mainloop()

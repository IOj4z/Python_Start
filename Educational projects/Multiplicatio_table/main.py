from tkinter import *


def showTable():
    num = num_box.get()
    num = int(num)
    value = 1
    for i in range(1, 11):
        a = i * num
        num_list.insert(END, (num, 'x', i, '=', a))
        value = value + 1
    num_box.delete(0, END)
    num_box.focus()


def clearList():
    num_box.delete(0, END)
    num_list.delete(0, END)
    num_box.focus()


window = Tk()
window.title('Mult-Table')
window.geometry('400x280')

label1 = Label(text='Enter a number: ')
label1.place(x=20, y=20, width=120, height=25)

num_box = Entry(text=0)
num_box.place(x=120, y=20, width=100, height=25)
num_box.focus()

button1 = Button(text='Show Table', command=showTable)
button1.place(x=250, y=20, width=120, height=25)

num_list = Listbox()
num_list.place(x=120, y=50, width=100, height=200)

button2 = Button(text='Clear Table', command=clearList)
button2.place(x=250, y=50, width=120, height=25)
window.mainloop()


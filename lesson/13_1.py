import csv

"""
Using the Books.csv file from Program 111, 
prompt the user for a new entry and append it to the end of the file. 
Bring out each line of the .csv file on a separate line.
"""

# file = open('Books.csv', 'a')
# book = input('Enter book name: ')
# author = input('Enter author name: ')
# year = input('Enter year: ')
# newRecord = book + ', ' + author + ', ' + year + '\n'
# file.write(str(newRecord))
# file.close()


"""
Using the Books.csv file, ask the user how many entries they want to add to the list, 
and provide him such an opportunity. 
After the data has been added, query the author and display all the books of the specified author from the list. 
If there are no books in the list this author, display the corresponding message.
"""
#
# num = int(input('How many books do you want to add: '))
# file = open('Books.csv', 'a')
# for i in range(0, num):
#     book = input('Enter book name: ')
#     author = input('Enter author name: ')
#     year = input('Enter year: ')
#     newRecord = book + ', ' + author + ', ' + year + '\n'
#     file.write(str(newRecord))
# file.close()
#
# findAuthor = input('Enter name author to find: ')
# file = open('Books.csv', 'r')
# count = 0
# for row in file:
#     if findAuthor in str(row):
#         print(row)
#         count = count + 1
# if count == 0:
#     print('There are no book bu author')
# file.close()

"""
Using the Books.csv file, prompt the user to enter a start and end year.
Print all books published in the given time interval.
"""
# file = list(csv.reader(open('Books.csv')))
# bookYearStart = int(input('Enter start year: '))
# bookYearEnd = int(input('Enter end year: '))
# tmp = []
# for row in file:
#     tmp.append(row)
# x = 0
# for row in tmp:
#     if int(tmp[x][2]) >= bookYearStart and int(tmp[x][2]) <= bookYearEnd:
#         print(tmp[x])
#     x = x + 1

"""
Using the Books.csv file, output the data with line numbers.
"""
# file = open('Books.csv', 'r')
# x = 1
# for row in file:
#     string = str(x) + ') ' + row
#     print(string)
#     x = x + 1

"""
Import the data from the Books.csv file into the list. List it out, 
prompt the user to choose which line they want to exclude, and delete it.
Ask the user what data he wants to change and provide him
appropriate opportunity. Write the data back to the .csv file, replacing the existing ones.
"""
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)


x = 0
for row in file:
    string = x, tmp[x]
    print(string)
    x = x + 1

print(tmp)
ids = int(input("Enter a row number to delete: "))
del tmp[ids]
x = 0
for row in tmp:
    display = x, tmp[x]
    print(display)
    x = x + 1

alter = int(input("Enter a row number to alter: "))
x = 0
for row in tmp[alter]:
    display = x, tmp[alter][x]
    print(display)
    x = x + 1

part = int(input("Which part do you want to change? "))
newdata = input("Enter new data: ")
tmp[alter][part] = newdata
print(tmp[alter])
file = open("Books.csv", "w")

x = 0
for row in tmp:
    newrecord = tmp[x][0] + ", " + tmp[x][1] + ", " + tmp[x][2] + "\n"
    file.write(newrecord)
    x = x+1
file.close()
"""
Create a simple math game that asks the user for a name and then generates two random questions. 
Save the name, questions entered, user responses, and final invoice in .csv file. 
Each time it is run, the program should add information to the .csv file without
overwriting existing data.
"""

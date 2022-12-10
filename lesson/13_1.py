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
file = list(csv.reader(open('Books.csv')))
bookYearStart = int(input('Enter start year: '))
bookYearEnd = int(input('Enter end year: '))
tmp = []
for row in file:
    tmp.append(row)
x = 0
for row in tmp:
    if int(tmp[x][2]) >= bookYearStart and int(tmp[x][2]) <= bookYearEnd:
        print(tmp[x])
    x = x + 1


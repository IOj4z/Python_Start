import sqlite3

"""
Create a SQL database named PhoneBook. 
The database must contain a Names table with the following data:
"""
# with sqlite3.connect('PhoneBook.db') as db:
#     cursor = db.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS  names(
#         id integer PRIMARY KEY,
#         f_name text NOT NULL,
#         sur_name text NOT NULL,
#         p_number integer
#         );""")
#
# f_name = input('Enter First Name: ')
# sur_name = input('Enter Surname: ')
# p_number = input('Enter Phone Number: ')
# cursor.execute("""INSERT INTO names(f_name,sur_name,p_number)
# VALUES (?,?,?)""", (f_name, sur_name, p_number))
# db.commit()


"""
Using the database
Write a program, which brings up the following menu:
main menu
1) View phone book
2) Add to phone book
3) Search for surname
4) Delete person from phone book
5) Quit
Enter your selection:
If the user selects item 1, he will be able to view the entire telephone book. 
If he chooses point 2, he will be able to add a new entry to the phone book. 
If selected point 3, the program prompts you to enter a surname,
and then outputs the records all people with the given last name. 
When choosing an item 4 program offers enter identifier
and removes the corresponding entry from the table.
When choosing item 5 the program ends.
Finally, when entering an invalid number,
an appropriate error message is displayed.
After every action the user must return to the menu until option 5 will be selected.
"""

#
# def v_pbook():
#     cursor.execute("SELECT * FROM names")
#     for x in cursor.fetchall():
#         print(x)
#
#
# def add_pbook():
#     f_name = input('Enter First Name: ')
#     sur_name = input('Enter Surname: ')
#     p_number = input('Enter Phone Number: ')
#     cursor.execute("""INSERT INTO names(f_name,sur_name,p_number)
#     VALUES (?,?,?)""", (f_name, sur_name, p_number))
#     db.commit()
#
#
# def search_surname(surname):
#     cursor.execute("SELECT * FROM names WHERE sur_name = ?", [surname])
#     for x in cursor.fetchall():
#         print(x)
#
#
# def delete_pbook():
#     v_pbook()
#     id_number = int(input('Enter num for delete: '))
#     cursor.execute('DELETE FROM names WHERE id = ?', [id_number])
#     db.commit()
#
#
# def quit_pbook():
#     return False
#
#
# def main():
#     while True:
#         print('Enter your selection: ')
#         list = ['1) View phone book', '2) Add to phone book', '3) Search for surname',
#                 '4) Delete person from phone book', '5) Quit']
#         for x in list:
#             print(x)
#         number = int(input('Enter number for action: '))
#         match number:
#             case 1:
#                 v_pbook()
#             case 2:
#                 add_pbook()
#             case 3:
#                 surname = input('Enter Surname: ')
#                 search_surname(surname)
#             case 4:
#                 delete_pbook()
#             case 5:
#                 print('Good bye!')
#                 return False
#             case _:
#                 print("Uncorrected")
#
#
# if __name__ == '__main__':
#     main()

"""
Create a SQL database named BookInfo for to store a list of authors and books written by them. 
It consists of two tables. The first table named Authors contains the following data:
BookInfo=[Authors['Name':['Agatha Christie', 'Cecelia Ahern', 'J. K. Rowling','Oscar Wilde'],
'Place of Birth':['Torquay', 'Dublin','Bristol','Dublin']]
"""

with sqlite3.connect('bookinfo.db') as db:
    cursor = db.cursor()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS authors(
#         name text NOT NULL,
#         place_bith text NOT NULL
#         );""")
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS books(
#     id integer PRIMARY KEY,
#     title text NOT NULL,
#     author text NOT NULL,
#     date_pub integer NOT NULL
#     );""")
#
# while range(1, 12):
#     title = input('Enter title: ')
#     author = input('Enter author name: ')
#     date_pub = int(input('Enter Date Published: '))
#
#     cursor.execute("""INSERT INTO books(title,author,date_pub ) VALUES (?, ?, ?)""", [title, author, date_pub])
#     db.commit()

"""
Print a list of authors with dates of birth. 
Prompt the user to enter a place of birth, and then
output the title, publication date and author's name for
all books by authors born in the specified location.
"""

# cursor.execute('SELECT * FROM authors')
# for x in cursor.fetchall():
#     print('author: ' + x[0] + ' birth place: ' + x[1])
#
# author_bplace = input('Enter author birth place: ')
#
# cursor.execute('SELECT books.title, authors.name, authors.place_bith, books.date_pub FROM books, '
#                'authors WHERE authors.name = books.author AND authors.place_bith=?', [author_bplace])
# for x in cursor.fetchall():
#     print(x)


"""
Prompt the user to enter a year. 
Print all books published after this year; 
list should be sorted by year of publication.
"""

# date = input('Enter date of publication: ')
# cursor.execute("""SELECT books.title, books.author,
# books.date_pub FROM books WHERE date_pub > ? ORDER BY date_pub""", [date])
# for x in cursor.fetchall():
#     print(x)


"""
Prompt the user to enter the author's name.
Save all books by this author in a text file; 
fields must be separated by hyphens, so the output should look something like this:
5 - Murder on the Orient Express - Agatha Christie - 1934
8 - The murder on the links - Agatha Christie - 1923
10 - The secret adversary - Agatha Christie - 1921
11 - The seven dials mystery - Agatha Christie - 1929
Open the text file and make sure the program works correctly.
"""

author_name = input('Enter author name: ')
books_doc = open('Books.txt', 'w')
cursor.execute("""SELECT * FROM books WHERE author=?""", [author_name])
for a in cursor.fetchall():
    books_doc.write(str(a[0]) + ' - ' + str(a[1]) + ' - ' + str(a[2]) + ' - ' + str(a[3]) + '\n')

books_doc.close()

books_doc = open('Books.txt', 'r')
books_doc.readable()
for x in books_doc:
    print(x)

books_doc.close()
db.close()
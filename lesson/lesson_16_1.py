import sqlite3

"""
Create a SQL database named PhoneBook. 
The database must contain a Names table with the following data:
"""
with sqlite3.connect('PhoneBook.db') as db:
    cursor = db.cursor()

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


def v_pbook():
    cursor.execute("SELECT * FROM names")
    for x in cursor.fetchall():
        print(x)


def add_pbook():
    f_name = input('Enter First Name: ')
    sur_name = input('Enter Surname: ')
    p_number = input('Enter Phone Number: ')
    cursor.execute("""INSERT INTO names(f_name,sur_name,p_number)
    VALUES (?,?,?)""", (f_name, sur_name, p_number))
    db.commit()


def search_surname(surname):
    cursor.execute("SELECT * FROM names WHERE sur_name = ?", [surname])
    for x in cursor.fetchall():
        print(x)


def delete_pbook():
    v_pbook()
    id_number = int(input('Enter num for delete: '))
    cursor.execute('DELETE FROM names WHERE id = ?', [id_number])
    db.commit()


def quit_pbook():
    return False


def main():
    while True:
        print('Enter your selection: ')
        list = ['1) View phone book', '2) Add to phone book', '3) Search for surname',
                '4) Delete person from phone book', '5) Quit']
        for x in list:
            print(x)
        number = int(input('Enter number for action: '))
        match number:
            case 1:
                v_pbook()
            case 2:
                add_pbook()
            case 3:
                surname = input('Enter Surname: ')
                search_surname(surname)
            case 4:
                delete_pbook()
            case 5:
                print('Good bye!')
                return False
            case _:
                print("Uncorrected")



if __name__ == '__main__':
    main()
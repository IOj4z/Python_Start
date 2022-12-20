import sqlite3

with sqlite3.connect('company.db') as db:
    cursor = db.cursor()
#
# cursor.execute(""" CREATE TABLE IF NOT EXISTS employees (
#     id integer PRIMARY KEY,
#     name text not NULL,
#     dept text NOT NULL,
#     salary integer);""")
#
# cursor.execute("""INSERT INTO employees(id,name,dept,salary) VALUES ('1', 'Bob', 'Sales', '25000')""")
# db.commit()

# newID = input('Enter ID number: ')
# newName = input('Enter name: ')
# newDept = input('Enter department: ')
# newSalary = input('Enter salary: ')
# cursor.execute("""INSERT INTO employees(id,name,dept,salary)
# VALUES (?,?,?,?)""", (newID, newName, newDept, newSalary))
# db.commit()


# cursor.execute("SELECT * FROM employees")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM employees")
# for x in cursor.fetchall():
#     print(x)

# cursor.execute('SELECT * FROM employees ORDER BY name')
# for x in cursor.fetchall():
#     print(x)


# cursor.execute('SELECT * FROM employees WHERE salary > 20000')
# for x in cursor.fetchall():
#     print(x)


# cursor.execute("SELECT * FROM employees WHERE dept = 'Sales'")
# print(cursor.fetchall())


# cursor.execute("""SELECT employees.id, employees.name, dept.manager
# FROM employees.dept WHERE employees.dept = dept.dept
# AND employees.salary > 20000""")

# cursor.execute("SELECT id , dept, manager FROM dept")


# whichDept = input('Enter a department: ')
# cursor.execute('SELECT * FROM employees WHERE dept=?', [whichDept])
# for x in cursor.fetchall():
#     print(x)


# cursor.execute("""SELECT employees.id, employees.name, dept.manager
# FROM employees, dept WHERE employees.dept=dept.dept""")


# cursor.execute("UPDATE employees SET name = 'Tony' WHERE id=4")
# db.commit()

# cursor.execute("UPDATE employees SET name = 'Tony' WHERE id=4")


cursor.execute('DELETE FROM employees WHERE id = 4')
db.commit()

db.close()

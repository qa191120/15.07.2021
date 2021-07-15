import sqlite3
from employee import *

conn = sqlite3.connect('company.db')

def create_employee_table():
    conn.execute('''
        CREATE TABLE EMPLOYEE
        (ID INT PRIMARY KEY NOT NULL, 
        NAME TEXT NOT NULL, AGE INT NOT NULL,
        ADDRESS CHAR(50), SALARY REAL)
        ''')

def insert_into_employee_table(e):
    conn.execute(f'''
        INSERT INTO EMPLOYEE 
        (ID,NAME,AGE,ADDRESS,SALARY)
         VALUES 
        ({e.id}, '{e.name}', {e.age}, '{e.address}', {e.salary})''')
    conn.commit()

    print("done")

def get_all_employees():
    result = conn.execute('SELECT * FROM EMPLOYEE')
    emp_result = []
    for row in result:
        e = Employee(row[0], row[1], row[2], row[3], row[4])
        emp_result.append(e)
    return emp_result

def get_employee_by_id(id):
    result = conn.execute(f'SELECT * FROM EMPLOYEE WHERE id = {id}')
    for row in result:
        e = Employee(row[0], row[1], row[2], row[3], row[4])
        return e
    return None

def update_employee(e, id):
    conn.execute(f'''
                 UPDATE EMPLOYEE SET NAME = '{e.name}', AGE = {e.age}, ADDRESS = '{e.address}', 
                    SALARY = {e.salary}   
                 WHERE ID = {id}''')
    conn.commit()

def delete_employee(id):
    # more generic more complex
    conn.execute(f'DELETE FROM EMPLOYEE WHERE ID = {id}')
    conn.commit()

def drop_employee_table():
    conn.execute("DROP TABLE EMPLOYEE;")
    conn.commit()

#emp1 = get_employee_by_id(1)
#print(emp1)

#e1 = Employee(1, 'Danny', 18, 'Tel Aviv', 20000)
#insert_into_employee_table(e1)
#e2 = Employee(2, 'Moshe', 30, 'Hertzelliya', 40000)
#insert_into_employee_table(e2)
#e2 = Employee(2, 'Moshe', 30, 'Hertzelliya', 45000)
#update_employee(e2, 2)
#e3 = Employee(3, 'Moshe', 30, 'Hertzelliya', 40000)
#insert_into_employee_table(e3)
#delete_employee(3)
print('========== ID is 2 ===============')
e2 = get_employee_by_id(2)
print(e2)
print('========== ALL ===============')
emp_list = get_all_employees()
for emp in emp_list:
    print(emp)

#drop_employee_table()
#create_employee_table()

# *etgar: copy this functions into DAO classz


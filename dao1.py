import sqlite3

conn = sqlite3.connect('company.db')

def create_employee_table():
    conn.execute('''
        CREATE TABLE EMPLOYEE
        (ID INT PRIMARY KEY NOT NULL, 
        NAME TEXT NOT NULL, AGE INT NOT NULL,
        ADDRESS CHAR(50), SALARY REAL)
        ''')

def insert_into_employee_table():
    conn.execute('''
        INSERT INTO EMPLOYEE 
        (ID,NAME,AGE,ADDRESS,SALARY)
         VALUES 
        (1, 'PAUL', 32, 'California', 25000.5)''')
    conn.execute('''
        INSERT INTO EMPLOYEE 
        (ID,NAME,AGE,ADDRESS,SALARY)
         VALUES 
        (2, 'Allen', 25, 'Texas', 23011.8)''')
    conn.commit()

    print("done")

def print_employee_table():
    result = conn.execute('SELECT * FROM EMPLOYEE')
    for row in result:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("AGE = ", row[2])
        print("ADDRESS = ", row[3])
        print("SALARY = ", row[4])
        print("=====================")

def update_employee():
    conn.execute("UPDATE EMPLOYEE SET SALARY = 30000 WHERE ID = 1")
    conn.commit()

def delete_employee():
    # more generic more complex
    conn.execute("DELETE FROM EMPLOYEE WHERE ID = 1")
    conn.commit()

def drop_employee_table():
    conn.execute("DROP TABLE EMPLOYEE;")
    conn.commit()

drop_employee_table()
create_employee_table()
insert_into_employee_table()
update_employee();
#delete_employee();
print_employee_table();

# change to auto increment
# insert_employee(name, age,address,salary)
# create class Employee (with id, name, age, address, salary)
# insert_employee( employee )
# get_employee(id) ==> employee
# get_all_employees() ==> [ employee1, employee2,... ]
# update employee (id, employee)
# delete_employee(id)
# *etgar: copy this functions into DAO classz

class Employee:
    def __init__(self, id, name, age, address, salary):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
    def __str__(self):
        return f'id: {id} name:{name} age:{age} address:{address} salary:{salary}'

import mysql.connector

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': 3306,
        'database': 'knights'
    }

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
cursor.execute("CREATE TABLE best_table (Name VARCHAR(255))")

add_employee = "INSERT INTO best_table " "(Name) " "VALUES (%s)"

data_employee = "Alice"
# Insert new employee
cursor.execute(add_employee, (data_employee,))

data_employee = "Bob"
cursor.execute(add_employee, (data_employee,))
# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()

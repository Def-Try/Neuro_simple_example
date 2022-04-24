import sqlite3
import pandas as pd

def createTableExcel():
    cxn = sqlite3.connect('mydb.db')
    wb = pd.read_excel('светофор.xlsm',sheet_name = 'Светофор')
    wb.to_sql(name='svet4',con=cxn,if_exists='replace',index=True)
    cxn.commit()
    cxn.close()

def create_connection(path):
    connection = None

    connection = sqlite3.connect(path)
    print("Connection to SQLite DB successful")
    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None

    cursor.execute(query)
    result = cursor.fetchall()
    return result

connection = create_connection("mydb.db")
select_users = "SELECT * from svet4"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

# createTableExcel()
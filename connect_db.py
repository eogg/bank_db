import mysql.connector
import database_functions

connection = mysql.connector.connect(user = 'root', database = 'bank_database',password = '113377')
cursor = connection.cursor()
testQuery = ("SELECT * FROM bank_database.user")
cursor.execute(testQuery)
for item in cursor:
    for thing in item:
        print(thing, end = ", ")
    print()
\




database_functions.getBalance()
database_functions.deposit(8999)

# By End of Week - Students have created SQL tables needed for the app and have successfully created all (or most) 
# functions for all tasks (check balance, deposit, withdraw, create account, delete account, modify account) 
# and create tables for account data.
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


acID = int(input("Enter your Account ID: "))
acPw = int(input("Enter your Pin Code: "))


database_functions.getBalance(acID, acPw)
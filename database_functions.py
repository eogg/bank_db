import mysql.connector

def getBalance():
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(item[0])
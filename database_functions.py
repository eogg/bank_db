import mysql.connector

def getBalance(accountID, accountPassword):
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {accountID} AND pin_code = {accountPassword}')
    for item in cursor:
        print(item[0])
import mysql.connector

connect = mysql.connector.connect(user = 'root', database = 'bank_database',password = '113377')

def getBalance(accountID, accountPassword):
    cursor = connect.cursor()
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {accountID} AND pin_code = {accountPassword}')
    for item in cursor:
        print(item[0])

def deposit(accountID, accountPassword, depo):
    cursor = connect.cursor()
    cursor.execute(f'UPDATE bank_database.user SET balance = balance + {depo} WHERE accountid = {accountID} AND pin_code = {accountPassword}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {accountID} AND pin_code = {accountPassword}')
    for item in cursor:
        print(f"Successfully deposited ${depo} to account number {accountID}. The new balance for account number {accountID} is " + item[0])
    
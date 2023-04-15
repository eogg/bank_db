import mysql.connector

connect = mysql.connector.connect(user = 'root', database = 'bank_database',password = '113377')
cursor = connect.cursor()

def getBalance():
    acID = int(input("Enter your Account ID: "))
    acPW = int(input("Enter your Pin Code: "))
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(item[0])

def deposit(depo):
    acID = int(input("Enter your Account ID: "))
    acPW = int(input("Enter your Pin Code: "))
    depo = int(input("How much would you like to deposit into your account?"))
    cursor.execute(f'UPDATE bank_database.user SET balance = balance + {depo} WHERE accountid = {acID} AND pin_code = {acPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(f'Successfully deposited ${depo} to account number {acID}. The new balance for account number {acID} is {item[0]}.')

def widthdraw(amt):
    acID = int(input("Enter your Account ID: "))
    acPW = int(input("Enter your Pin Code: "))
    depo = int(input("How much would you like to deposit into your account?"))
    cursor.execute(f'UPDATE bank_database.user SET balance = balance - {amt} WHERE accountid = {acID} AND pin_code = {acPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(f'Successfully widthdrew ${amt} to account number {acID}. The new balance for account number {acID} is {item[0]}.')
    
    
# def update_account(accountID, accountPassword):

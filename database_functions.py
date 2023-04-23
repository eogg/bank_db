import mysql.connector
import random

connect = mysql.connector.connect(user = 'root', database = 'bank_database',password = '113377')
cursor = connect.cursor(buffered=True)

def getBalance():
    acID = int(input("Enter your Account ID: "))
    acPW = int(input("Enter your Pin Code: "))
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(item[0])

def deposit():
    acID = int(input("Enter your Account ID: "))
    acPW = int(input("Enter your Pin Code: "))
    depo = int(input("How much would you like to deposit into your account? "))
    cursor.execute(f'UPDATE bank_database.user SET balance = balance + {depo} WHERE accountid = {acID} AND pin_code = {acPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(f'Successfully deposited ${depo} to account number {acID}. The new balance for account number {acID} is {item[0]}.')

def widthdraw():
    acID = int(input("Enter your Account ID: "))
    acPW = int(input("Enter your Pin Code: "))
    amt = int(input("How much would you like to withdraw from your account? "))
    cursor.execute(f'UPDATE bank_database.user SET balance = balance - {amt} WHERE accountid = {acID} AND pin_code = {acPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(f'Successfully widthdrew ${amt} to account number {acID}. The new balance for account number {acID} is {item[0]}.')
    
def create_account():
    username = str(input("What name would you like the account to be under? "))
    amt = int(input("How much would you like to initially deposit into your account? "))
    indob = input("Please enter your date of birth in the format of mm/dd/yyyy. ")
    while True:
        pin = int(input("Please enter the pin you'd like to use for your account: "))
        pin2 = int(input("Please enter the pin again. "))
        if(pin == pin2):
            break
        else:
            print("Please try again.")
            continue
    while True:
        accid = random.randint(100000, 999999)
        check = cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {accid}')
        if(check is None):
            break
        else: 
            continue
    cursor.execute(f"INSERT INTO bank_database.user (accountid, accountname, balance, dob, pin_code) VALUES ({accid}, \"{username}\", {amt}, \"{indob}\", {pin})")

def printOutEntireTable():
    testQuery = ("SELECT * FROM bank_database.user")
    cursor.execute(testQuery)
    for item in cursor:
        for thing in item:
            print(thing, end = ", ")
        print()
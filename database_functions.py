import mysql.connector
import random
import ui_functions
import passwordIn

connect = mysql.connector.connect(user = 'root', database = 'bank_database',password = passwordIn.password)
cursor = connect.cursor(buffered=True)

def getBalance():
    ui_functions.clear()
    acID = int(input("Enter your Account ID: "))
    acPW = int(input("Enter your 6 Digit Pin Code: "))
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(item[0])

def deposit():
    ui_functions.clear()
    while True:
        acID = int(input("Enter your Account ID: "))
        cursor.execute(f'SELECT accountid FROM bank_database.user')
        if(cursor is None):
            ui_functions.clear()
            print("The account ID you input does not exist, please try again")
            continue
        acPW = int(input("Enter your 6 Digit Pin Code: "))
        cursor.execute(f'SELECT * FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
        if(cursor is None):
            ui_functions.clear()
            print("The account ID you input does not match up with the account pin, please try again.")
            continue
        else: 
            break
    depo = int(input("How much would you like to deposit into your account? "))
    cursor.execute(f'UPDATE bank_database.user SET balance = balance + {depo} WHERE accountid = {acID} AND pin_code = {acPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(f'Successfully deposited ${depo} to account number {acID}. The new balance for account number {acID} is {item[0]}.')
    connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!

def widthdraw():
    ui_functions.clear()
    acID = int(input("Enter your Account ID: "))
    acPW = int(input("Enter your 6 Digit Pin Code: "))
    amt = int(input("How much would you like to withdraw from your account? "))
    cursor.execute(f'UPDATE bank_database.user SET balance = balance - {amt} WHERE accountid = {acID} AND pin_code = {acPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {acID} AND pin_code = {acPW}')
    for item in cursor:
        print(f'Successfully widthdrew ${amt} to account number {acID}. The new balance for account number {acID} is {item[0]}.')
    connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
    
def create_account():
    ui_functions.clear()
    username = str(input("What name would you like the account to be under? "))
    indob = input("Please enter your date of birth in the format of mm/dd/yyyy. ")
    amt = int(input("How much would you like to initially deposit into your account? "))
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
        cursor.execute(f'SELECT * FROM bank_database.user WHERE accountid = {accid}')
        if(cursor is None):
            break
        else: 
            continue
    cursor.execute(f"INSERT INTO bank_database.user (accountid, accountname, balance, dob, pin_code) VALUES ({accid}, \"{username}\", {amt}, \"{indob}\", {pin})")
    connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!

# def modify_name():
#     ui_functions.clear()
#     accId = str(input("What is your account ID?"))
#     while True:
#         accPw = input("What is your account Pin?")
#         accPw2 = input("Enter your Pin again.")
#         if accPw != accPw2:
#             print("The pins you entered do not match, try again.")
#             continue
#         else:
#             break
#     cursor.execute(f"SELECT * FROM bank_database.user WHERE accountid = {accId} AND pin_code = {accPw}")
#     for item in cursor:


def printOutEntireTable():
    ui_functions.clear()
    testQuery = ("SELECT * FROM bank_database.user")
    cursor.execute(testQuery)
    for item in cursor:
        for thing in item:
            print(thing, end = ", ")
        print()
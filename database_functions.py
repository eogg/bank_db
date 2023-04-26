import mysql.connector
import random
import ui_functions
import passwordIn
import os

connect = mysql.connector.connect(user = 'root', database = 'bank_database',password = passwordIn.password)
cursor = connect.cursor(buffered=True)
logInAccID = 0
logInACCPW = 0


def clear_console():
    os.system('cls')
# def clear():
#     os.system("clear")

def getBalance():
    global logInAccID
    global logInACCPW
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    for item in cursor:
        print(f"Your account balance is ${item[0]}")

def deposit():
    cursor.reset()
    global logInAccID
    global logInACCPW
    depo = int(input("How much would you like to deposit into your account? "))
    cursor.execute(f'UPDATE bank_database.user SET balance = balance + {depo} WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    for item in cursor:
        print(f'Successfully deposited ${depo} to account number {logInAccID}. The new balance for account number {logInAccID} is {item[0]}.')
    connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!

def widthdraw():
    global logInAccID
    global logInACCPW
    amt = int(input("How much would you like to withdraw from your account? "))
    cursor.execute(f'UPDATE bank_database.user SET balance = balance - {amt} WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    for item in cursor:
        print(f'Successfully widthdrew ${amt} to account number {logInAccID}. The new balance for account number {logInACCPW} is {item[0]}.')
    connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
    
def create_account():
    cursor.reset()
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
        accID = random.randint(100000, 999999)
        rows_count = cursor.execute(f"SELECT EXISTS(SELECT * FROM bank_database.user WHERE accountid = {accID})")
        if(rows_count is None):
            break
        else: 
            continue
    cursor.execute(f"INSERT INTO bank_database.user (accountid, accountname, balance, dob, pin_code) VALUES ({accID}, \"{username}\", {amt}, \"{indob}\", {pin})")
    print("Account successfully created!")
    connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!

def logIn():
    global logInAccID
    global logInACCPW
    cursor.reset()
    while True:
        logInAccID = input("Please enter your account ID: ")
        logInACCPW = input("Please enter your account Pin: ")
        cursor.execute(f'SELECT accountid FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        temp = 0
        for thing in cursor:
            for thingy in thing:
                temp = thingy
        if(temp == 0):
            print("Invalid username or password, try again.")
            continue
        else:
            break
    cursor.execute(f'SELECT accountname FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    for item in cursor:
        print(f"Successfully logged into {item[0]}'s account.")
    ui_functions.user_log_in_selection_menu()

def logOut():
    global logInAccID
    global logInACCPW
    logInACCPW = 0
    logInAccID = 0
    ui_functions.user_selection_menu()

# def modify_name():
#     global logInAccID
#     global logInACCPW

#     cursor.execute(f"SELECT * FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}")
#     for item in cursor:



def printOutEntireTable():
    clear_console()
    testQuery = ("SELECT * FROM bank_database.user")
    cursor.execute(testQuery)
    for item in cursor:
        for thing in item:
            print(thing, end = ", ")
        print()
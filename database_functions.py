import mysql.connector
import random
import ui_functions
import passwordIn
import os

connect = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    database = 'bank_database',
    password = passwordIn.password)

cursor = connect.cursor(buffered=True)
logInAccID = 0
logInACCPW = 0


# def clear_console():
#     os.system('cls')
def clear_console():
    os.system("clear")

def getBalance():
    global logInAccID
    global logInACCPW
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    for item in cursor:
        print(f"Your account balance is ${item[0]}")
    exitProgram()
    ui_functions.backToUserSignInMenu("u")

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
    exitProgram()
    ui_functions.backToUserSignInMenu("u")

def widthdraw():
    global logInAccID
    global logInACCPW
    while True:
        cursor.reset()
        amt = int(input("How much would you like to withdraw from your account? "))
        cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        balance = 0
        for item in cursor:
            for thing in item:
                balance = thing
        if amt < balance and amt > 0:
            cursor.execute(f'UPDATE bank_database.user SET balance = balance - {amt} WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
            cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
            for item in cursor:
                print(f'Successfully widthdrew ${amt} to account number {logInAccID}. The new balance for account number {logInACCPW} is {item[0]}.')
            connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
            exitProgram()
            ui_functions.backToUserSignInMenu("u")
            break
        else:
            print("The amount of money you're trying to withdraw is larger than your balance, please try again.")
    
    
def create_account(accType):
    global logInAccID
    global logInACCPW
    if accType == "u":
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
        logInAccID = accID
        logInACCPW = pin
        exitProgram()
        ui_functions.backToUserSignInMenu("u")
    elif accType == "a":
        cursor.reset()
        username = str(input("What name would you like the account to be under? "))
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
            accID = random.randint(100000, 999999)
            rows_count = cursor.execute(f"SELECT EXISTS(SELECT * FROM bank_database.admin WHERE accountid = {accID})")
            if(rows_count is None):
                break
            else: 
                continue
        cursor.execute(f"INSERT INTO bank_database.admin (accountid, accountname, dob, pin_code) VALUES ({accID}, \"{username}\", \"{indob}\", {pin})")
        print("Account successfully created!")
        connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
        logInAccID = accID
        logInACCPW = pin
        exitProgram()
        ui_functions.backToUserSignInMenu("a")

def delete_account():
    cursor.reset()
    global logInACCPW
    global logInAccID
    sure = str(input("Are you sure? y/n: "))
    if sure == "y":
        cursor.execute(f'DELETE FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        print("Account successfully deleted.")
        logInAccID = 0
        logInACCPW = 0
        connect.commit()
    else:
        print("Account deletion not completed.")
    exitProgram()

def logIn(accType):
    if accType == "u":
        global logInAccID
        global logInACCPW
        while True:
            cursor.reset()
            logInAccID = input("Please enter your account ID: ")
            logInACCPW = input("Please enter your account PIN: ")
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
        exitProgram()
        ui_functions.backToUserSignInMenu("u")
    elif accType == "a":
        while True:
            cursor.reset()
            logInAccID = input("Please enter your admin account ID: ")
            logInACCPW = input("Please enter your admin accoount PIN: ")
            cursor.execute(f'SELECT accountid FROM bank_database.admin WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
            temp = 0
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                print("Invalid username or password, try again.")
                continue
            else:
                break
        cursor.execute(f'SELECT accountname FROM bank_database.admin WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        for item in cursor:
            print(f"Successfully logged into {item[0]}'s account.")
        ui_functions.backToUserSignInMenu("a")
        exitProgram()

def logOut():
    global logInAccID
    global logInACCPW
    logInACCPW = 0
    logInAccID = 0
    exitProgram()

def modify_name(accType):
    global logInAccID
    global logInACCPW
    if accType == "u":
        newName = str(input("Enter the new name of the account: "))
        cursor.execute(f'UPDATE bank_database.user SET accountname = \"{newName}\" WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        print(f"Successfully changed the name of account {logInAccID} to {newName}")
        exitProgram()
        ui_functions.backToUserSignInMenu("u")
    elif accType == "a":
        clear_console()
        print("\nWould you like to:")
        print("1. Change the name of a user's account")
        print("2. Change the name of another admin's account")
        print("3. Change the name of your own account")
        while True:
            try:
                choice = input("Choose the number next to the action you want: ")
                break
            except ValueError:
                print("That is not a valid choice, please try again.")
        
        newName = str(input("Enter the new name of the account: "))
        cursor.execute(f'UPDATE bank_database.user SET accountname = \"{newName}\" WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        print(f"Successfully changed the name of account {logInAccID} to {newName}")
        exitProgram()
        ui_functions.backToUserSignInMenu("u")

def modify_pin():
    global logInAccID
    global logInACCPW
    newPin = input("Enter the new pin of the account: ")
    cursor.execute(f'UPDATE bank_database.user SET pin_code = {newPin} WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    print(f"Successfully changed the pin of account {logInAccID} to {newPin}") 
    exitProgram()
    ui_functions.backToUserSignInMenu("u")

def modify_account(accType):
    while True:
        try:
            choice = input("Would you like to update the name of an account (1) or the pin (2)?: ")
            break
        except ValueError: 
            print("That is not a valid choice, please try again.")
            
    if choice == 1:
        modify_name(accType)
    elif choice == 2:
        modify_pin(accType)
    else:
        print("That's not a valid choice, please try again.")

def printOutEntireTable():
    clear_console()
    testQuery = ("SELECT * FROM bank_database.user")
    cursor.execute(testQuery)
    for item in cursor:
        for thing in item:
            print(thing, end = ", ")
        print()

def exitProgram():
    while True:
        sure = str(input("Would you like keep going? y/n: "))
        if sure.lower() == "n":
            print("Thank you for using this banking app.")
            exit()
        elif sure.lower() == "y":
            break
        else:
            print("That option is not valid, please try again.")



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
logInAdminID = 0
logInAdminPW = 0


# def clear_console():
#     os.system('cls')
def clear_console():
    os.system("clear")

def getBalance():
    cursor.reset()
    global logInAccID
    global logInACCPW
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    for thing in cursor:
        for item in thing:
            temp = item
    print(f"\nYour account balance is ${temp}")
    exitProgram()
    ui_functions.backToUserSignInMenu("u")

def deposit():
    cursor.reset()
    global logInAccID
    global logInACCPW
    while True:
        try:
            depo = int(input("\nHow much would you like to deposit into your account? "))
        except ValueError:
            print("That's not a valid amount, please try again.")
        if depo > 0:
            break
    cursor.execute(f'UPDATE bank_database.user SET balance = balance + {depo} WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    for item in cursor:
        print(f'\nSuccessfully deposited ${depo} to account number {logInAccID}. The new balance for account number {logInAccID} is ${item[0]}.')
    connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
    exitProgram()
    ui_functions.backToUserSignInMenu("u")

def widthdraw():
    global logInAccID
    global logInACCPW
    while True:
        cursor.reset()
        while True:
            try:
                amt = int(input("\nHow much would you like to withdraw from your account? "))
                break
            except ValueError:
                print("That is not a valid amount, please try again.")
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
    global logInAdminPW
    global logInAdminID
    if accType == "u":
        cursor.reset()
        username = str(input("What name would you like the account to be under? "))
        indob = str(input("Please enter your date of birth in the format of mm/dd/yyyy. "))
        while True:
            try:
                amt = int(input("How much would you like to initially deposit into your account? "))
                break
            except ValueError:
                print("That is not a valid amount, please try again.")
        while True:
            while True:
                try:
                    pin = int(input("Please enter the pin you'd like to use for your account: "))
                    break
                except ValueError:
                    print("That is not a valid pin, try again.") 
            while True:
                try:
                    pin2 = int(input("Please enter the pin again: "))
                    break
                except ValueError:
                    print("That is not a valid pin, try again.") 
            if(pin == pin2):
                break
            else:
                print("The two pins do not match, try again.")
                continue

        while True:
            cursor.reset()
            accID = random.randint(100000, 999999)
            cursor.execute(f"SELECT EXISTS(SELECT * FROM bank_database.user WHERE accountid = {accID})")
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                break
            else: 
                continue
        cursor.execute(f"INSERT INTO bank_database.user (accountid, accountname, balance, dob, pin_code) VALUES ({accID}, \"{username}\", {amt}, \"{indob}\", {pin})")
        clear_console()
        print("\nAccount successfully created!")
        connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
        logInAccID = accID
        logInACCPW = pin
        cursor.reset()
        cursor.execute(f"SELECT * FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}")
        for item in cursor:
            temp = item
        print(f"Account ID: {temp[0]}")
        print(f"Account Name: {temp[1]}")
        print(f"Account DOB: {temp[2]}")
        print(f"Account PIN: {temp[3]}")
        print(f"Account Balance: ${temp[4]}")
        exitProgram()
        ui_functions.backToUserSignInMenu("u")
    elif accType == "a":
        cursor.reset()
        username = str(input("What name would you like the account to be under? "))
        indob = str(input("Please enter your date of birth in the format of mm/dd/yyyy. "))
        while True:
            while True:
                try:
                    pin = int(input("Please enter the pin you'd like to use for your account: "))
                    break
                except ValueError:
                    print("That is not a valid pin, try again.") 
            while True:
                try:
                    pin2 = int(input("Please enter the pin again: "))
                    break
                except ValueError:
                    print("That is not a valid pin, try again.") 
            if(pin == pin2):
                break
            else:
                print("The two pins do not match, try again.")
                continue

        while True:
            cursor.reset()
            accID = random.randint(100000, 999999)
            cursor.execute(f"SELECT EXISTS(SELECT * FROM bank_database.admin WHERE accountid = {accID})")
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                break
            else: 
                continue
        cursor.execute(f"INSERT INTO bank_database.admin (accountid, accountname, dob, pin_code) VALUES ({accID}, \"{username}\", \"{indob}\", {pin})")
        clear_console()
        print("Admin account successfully created!")
        connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
        logInAdminID = accID
        logInAdminPW = pin
        cursor.reset()
        cursor.execute(f"SELECT * FROM bank_database.admin WHERE accountid = {logInAdminID} AND pin_code = {logInAdminPW}")
        for item in cursor:
            temp = item
        print(f"Admin Account ID: {temp[0]}")
        print(f"Account Name: {temp[1]}")
        print(f"Account DOB: {temp[2]}")
        print(f"Admin Account PIN: {temp[3]}")
        exitProgram()
        ui_functions.backToUserSignInMenu("a")

def delete_account(accType, inType):
    global logInAccID
    global logInACCPW
    global logInAdminID
    global logInAdminPW
    if accType == "a" and inType == 0:
        while True:
            cursor.reset()
            logInAccID = input("Please enter the user's account ID: ")
            logInACCPW = input("Please enter the user's account PIN: ")
            cursor.execute(f'SELECT EXISTS(SELECT accountid FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW})')
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                print("Invalid username or password, try again.")
                continue
            else:
                delete_account("u", 0)
                break
    if accType == "u":
        cursor.reset()
        sure = str(input("Are you sure? y/n: "))
        if sure == "y":
            cursor.execute(f'DELETE FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
            print("\nUser account successfully deleted.")
            logInAccID = 0
            logInACCPW = 0
            connect.commit()
        else:
            print("\nUser account deletion not completed.")
        exitProgram()
        ui_functions.backToUserSignInMenu("u")
    elif accType == "a":
        cursor.reset()
        sure = str(input("Are you sure? y/n: "))
        if sure == "y":
            cursor.execute(f'DELETE FROM bank_database.admin WHERE accountid = {logInAdminID} AND pin_code = {logInAdminPW}')
            print("\nAdmin account successfully deleted.")
            logInAccID = 0
            logInACCPW = 0
            connect.commit()
        else:
            print("\nAdmin account deletion not completed.")
        exitProgram()
        ui_functions.backToUserSignInMenu("a")

def logIn(accType):
    global logInAccID
    global logInACCPW
    global logInAdminID
    global logInAdminPW
    if accType == "u":
        while True:
            cursor.reset()
            logInAccID = input("Please enter your account ID: ")
            logInACCPW = input("Please enter your account PIN: ")
            cursor.execute(f'SELECT EXISTS(SELECT accountid FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW})')
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                print("Invalid username or password, try again.")
                continue
            else:
                break
        cursor.execute(f'SELECT accountname FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        for item in cursor:
            print(f"Successfully logged into {item[0]}'s account.")
        ui_functions.backToUserSignInMenu("u")
    else:
        while True:
            cursor.reset()
            logInAdminID = input("Please enter your admin account ID: ")
            logInAdminPW = input("Please enter your admin accoount PIN: ")
            cursor.execute(f'SELECT EXISTS(SELECT accountid FROM bank_database.admin WHERE accountid = {logInAdminID} AND pin_code = {logInAdminPW})')
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                print("Invalid username or password, try again.")
                continue
            else:
                break
        cursor.execute(f'SELECT accountname FROM bank_database.admin WHERE accountid = {logInAdminID} AND pin_code = {logInAdminPW}')
        for item in cursor:
            print(f"Successfully logged into {item[0]}'s account.")
        ui_functions.backToUserSignInMenu("a")
        
def logOut():
    global logInAccID
    global logInACCPW
    logInACCPW = 0
    logInAccID = 0
    exitProgram()

def modify_name(accType, inType):
    global logInAccID
    global logInACCPW
    global logInAdminID
    global logInAdminPW
    if accType == "u" and inType == 0:
        while True:
            cursor.reset()
            logInAccID = input("Please enter the user's account ID: ")
            logInACCPW = input("Please enter the user's account PIN: ")
            cursor.execute(f'SELECT EXISTS(SELECT accountid FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW})')
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                print("Invalid username or password, try again.")
                continue
            else:
                break
    if accType == "u":
        clear_console()
        newName = str(input("Enter the new name of the account: "))
        cursor.execute(f'UPDATE bank_database.user SET accountname = \"{newName}\" WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        print(f"\nSuccessfully changed the name of user account {logInAccID} to {newName}")
        connect.commit()
        exitProgram()
        ui_functions.backToUserSignInMenu("u")
    elif accType == "a":
        clear_console()
        newName = str(input("Enter the new name of the admin account: "))
        cursor.execute(f'UPDATE bank_database.admin SET accountname = \"{newName}\" WHERE accountid = {logInAdminID} AND pin_code = {logInAdminPW}')
        print(f"\nSuccessfully changed the name of account {logInAdminID} to {newName}")
        connect.commit()
        exitProgram()
        ui_functions.backToUserSignInMenu("a")

def modify_pin(accType, inType):
    global logInAccID
    global logInACCPW
    global logInAdminID
    global logInAdminPW
    if accType == "u" and inType == 0:
        while True:
            cursor.reset()
            while True:
                try: 
                    logInAccID = input("Please enter the user's account ID: ")
                    break
                except ValueError:
                    print("That is not a valid account ID, please try again.")
            while True:
                try: 
                    logInACCPW = input("Please enter the user's account PIN: ")
                    break
                except ValueError:
                    print("That is not a valid account account PIN, please try again.")
            cursor.execute(f'SELECT EXISTS(SELECT accountid FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW})')
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                print("Invalid username or password, try again.")
                continue
            else:
                break
    if accType == "u":
        newPin = input("Enter the new pin of the user account: ")
        cursor.execute(f'UPDATE bank_database.user SET pin_code = {newPin} WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        print(f"\nSuccessfully changed the pin of user account {logInAccID} to {newPin}") 
        connect.commit()
        exitProgram()
        ui_functions.backToUserSignInMenu("u")
    else:
        newPin = input("Enter the new pin of your admin account: ")
        cursor.execute(f'UPDATE bank_database.admin SET pin_code = {newPin} WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        print(f"\nSuccessfully changed the pin of admin account {logInAccID} to {newPin}") 
        connect.commit()
        exitProgram()
        ui_functions.backToUserSignInMenu("a")

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
        sure = str(input("\nWould you like keep going? y/n: "))
        if sure.lower() == "n":
            clear_console()
            print("Thank you for using this banking app.")
            exit()
        elif sure.lower() == "y":
            break
        else:
            print("That option is not valid, please try again.")
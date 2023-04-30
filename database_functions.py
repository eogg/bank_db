import mysql.connector
import random
import ui_functions
import passwordIn
import os

#CONNECTING TO MYSQL
connect = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    database = 'bank_database',
    password = passwordIn.password)
#CURSOR FOR QUERIES
cursor = connect.cursor(buffered=True)

#LOG IN VARIABLES - STORE USER'S ACCOUNT NUMBER AND PIN FOR TRANSACTIONS AND MODIFICATIONS
logInAccID = 0
logInACCPW = 0
logInAdminID = 0
logInAdminPW = 0

#CLEAR CONSOLE FOR WIN PC
def clear_console():
    os.system('cls')

#CLEAR CONSOLE FOR MACBOOK
# def clear_console():
#     os.system("clear")

#PRINTS ACCOUNT BALANCE
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

#ALLOWS FOR DEPOSIT INTO USER ACCOUNT
def deposit():
    cursor.reset()
    global logInAccID
    global logInACCPW
    depo = 0
    while True:
        try:
            depo = int(input("\nHow much would you like to deposit into your account? "))
        except ValueError:
            print("That's not a valid amount, please try again.")
        if(depo > 0):
            break
        else: 
            print("That's not a valid amount, please try again.")
    cursor.execute(f'UPDATE bank_database.user SET balance = balance + {depo} WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    cursor.execute(f'SELECT balance FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
    for item in cursor:
        print(f'\nSuccessfully deposited ${depo} to account number {logInAccID}. The new balance for account number {logInAccID} is ${item[0]}.')
    connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
    exitProgram()
    ui_functions.backToUserSignInMenu("u")

#ALLOWS FOR WITHDRAWAL FROM USER ACCOUNT
def withdraw():
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
                print(f'\nSuccessfully withdrew ${amt} to account number {logInAccID}. The new balance for account number {logInACCPW} is ${item[0]}.')
            connect.commit() #ESSENTIAL PIECE OF CODE TO ENSURE CHANGES ARE PERMANENT!
            exitProgram()
            ui_functions.backToUserSignInMenu("u")
            break
        elif amt < 0:
            print("That is not a valid amount, please try again.")
        else:
            print("The amount of money you're trying to withdraw is larger than your balance, please try again.")

#CREATES ACCOUNT USING {accType}, WHICH CHOOSES WHAT TYPE OF ACCOUNT TO BE MADE
def create_account(accType):
    global logInAccID
    global logInACCPW
    global logInAdminPW
    global logInAdminID
    if accType == "u":
        cursor.reset()
        while True:
            username = str(input("What name would you like the account to be under? "))
            if username == "" or username == " ":
                print("Please enter a name.")
            else:
                break
        while True:
            indob = str(input("Please enter your date of birth in the format of mm/dd/yyyy. "))
            if indob == "" or indob == " ":
                print("Please enter a valid date of birth.")
            else:
                break
        while True:
            try:
                amt = int(input("How much would you like to initially deposit into your account? "))
                if amt <= 0:
                    print("That is not a valid amount, please try again.")
                else:
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
        print(f"Account Name: {temp[1]}")
        print(f"Account ID: {temp[0]}")
        print(f"Account PIN: {temp[3]}")
        print(f"Account DOB: {temp[2]}")
        print(f"Account Balance: ${temp[4]}")
        exitProgram()
        ui_functions.backToUserSignInMenu("u")
    elif accType == "a":
        cursor.reset()
        while True:
            username = str(input("What name would you like the account to be under? "))
            if username == "" or username == " ":
                print("Please enter a name.")
            else:
                break
        while True:
            indob = str(input("Please enter your date of birth in the format of mm/dd/yyyy. "))
            if indob == "" or indob == " ":
                print("Please enter a valid date of birth.")
            else:
                break
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

#DELES ACCOUNT USING {accType}, WHICH LETS ADMIN ACCOUNTS DELETE USER ACCOUNTS
def delete_account(accType, inType):
    global logInAccID
    global logInACCPW
    global logInAdminID
    global logInAdminPW
    if accType == "a" and inType == 0:
        while True:
            cursor.reset()
            while True:
                try:
                    logInAccID = input("Please enter the user's account ID: ")
                    break
                except ValueError:
                    print("Please enter a valid Account ID.")
            while True:
                try:
                    logInACCPW = input("Please enter the user's account PIN: ")
                    break
                except ValueError:
                    print("Please enter a valid Account PIN.")
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
        if inType == 1:
            ui_functions.home_selection_menu()
        else:
            ui_functions.backToUserSignInMenu("a")
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
        ui_functions.home_selection_menu()

#LOGS IN
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

#LOGS OUT AND RETURNS TO HOME MENU     
def logOut():
    global logInAccID
    global logInACCPW
    logInACCPW = 0
    logInAccID = 0
    ui_functions.home_selection_menu()

#ALLOWS FOR THE MODIFICATION OF ACCOUNT NAMES, ADMIN CAN CHANGE BOTH THEIR NAME AND A USER'S NAME
def modify_name(accType, inType):
    global logInAccID
    global logInACCPW
    global logInAdminID
    global logInAdminPW
    if accType == "a" and inType == 0:
        while True:
            cursor.reset()
            while True:
                try:
                    logInAccID = int(input("Please enter the user's account ID: "))
                    break
                except ValueError:
                    print("Please enter a valid account ID.")
            while True:
                try:
                    logInACCPW = int(input("Please enter the user's account PIN: "))
                    break
                except ValueError:
                    print("Please enter a valid account PIN.")
            cursor.execute(f'SELECT EXISTS(SELECT accountid FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW})')
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                print("Invalid username or password, try again.")
                continue
            else:
                modify_name("u", 2)
    if accType == "u":
        clear_console()
        while True:
            newName = str(input("Enter the new name of the account: "))
            if len(newName) > 0:
                break
            else:
                print("Please enter a name.")
        cursor.execute(f'UPDATE bank_database.user SET accountname = \"{newName}\" WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        print(f"\nSuccessfully changed the name of user account {logInAccID} to {newName}")
        connect.commit()
        exitProgram()
        if inType == 2:

            ui_functions.backToUpdateMenu("a")
        else: 
            ui_functions.backToUpdateMenu("u")
    elif accType == "a":
        clear_console()
        while True:
            newName = str(input("Enter the new name of the account: "))
            if len(newName) > 0:
                break
            else:
                print("Please enter a name.")
        cursor.execute(f'UPDATE bank_database.admin SET accountname = \"{newName}\" WHERE accountid = {logInAdminID} AND pin_code = {logInAdminPW}')
        print(f"\nSuccessfully changed the name of account {logInAdminID} to {newName}")
        connect.commit()
        exitProgram()
        ui_functions.backToUpdateMenu("a")

#ALLOWS FOR THE MODIFICATION OF ACCOUNT PINS, ADMIN CAN CHANGE BOTH THEIR PIN AND A USER'S PIN
def modify_pin(accType, inType):
    global logInAccID
    global logInACCPW
    global logInAdminID
    global logInAdminPW
    if accType == "a" and inType == 0:
        while True:
            cursor.reset()
            while True:
                try:
                    logInAccID = int(input("Please enter the user's account ID: "))
                    break
                except ValueError:
                    print("Please enter a valid account ID.")
            while True:
                try:
                    logInACCPW = int(input("Please enter the user's account PIN: "))
                    break
                except ValueError:
                    print("Please enter a valid account PIN.")
            cursor.execute(f'SELECT EXISTS(SELECT accountid FROM bank_database.user WHERE accountid = {logInAccID} AND pin_code = {logInACCPW})')
            for item in cursor:
                for thing in item:
                    temp = thing
            if(temp == 0):
                print("Invalid username or password, try again.")
                continue
            else:
                modify_pin("u", 2)
    if accType == "u":
        while True:
                try:
                    newPin = int(input("Please enter the new pin of the account: "))
                    break
                except ValueError:
                    print("That is not a valid pin, try again.") 
        cursor.execute(f'UPDATE bank_database.user SET pin_code = {newPin} WHERE accountid = {logInAccID} AND pin_code = {logInACCPW}')
        print(f"\nSuccessfully changed the pin of user account {logInAccID} to {newPin}") 
        connect.commit()
        exitProgram()
        if inType == 2:
            ui_functions.backToUpdateMenu("a")
        else:
            ui_functions.backToUpdateMenu("u")
    else:
        while True:
                try:
                    newPin = int(input("Please enter the pin you'd like to use for your account: "))
                    break
                except ValueError:
                    print("That is not a valid pin, try again.") 
        cursor.execute(f'UPDATE bank_database.admin SET pin_code = {newPin} WHERE accountid = {logInAdminID} AND pin_code = {logInAdminPW}')
        print(f"\nSuccessfully changed the pin of admin account {logInAdminID} to {newPin}") 
        connect.commit()
        exitProgram()
        ui_functions.backToUpdateMenu("a")

#PRINTS OUT THE ENTIRE TABLE
def printOutEntireTable():
    clear_console()
    testQuery = ("SELECT * FROM bank_database.user")
    cursor.execute(testQuery)
    for item in cursor:
        for thing in item:
            print(thing, end = ", ")
        print()

#PROMTS ASKING IF THEY WANT TO EXIT, IF INPUT "y" == PROGRAM WILL BE EXITED.
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
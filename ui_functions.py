import database_functions

def user_selection_menu():
    database_functions.clear_console()
    print("\nWould you like to:")
    print("1. Create an Account")
    print("2. Log in")
    print("3. Log in as administrator")
    print("4. Exit baking system")
    home_user_select()
    
def user_log_in_selection_menu():
    database_functions.clear_console()
    print("\nWould you like to:")
    print("1. Get balance")
    print("2. Make a deposit")
    print("3. Widthdraw from account")
    print("4. Update account information")
    print("5. Delete account")
    print("6. Log out")
    logIn_user_select()

def modification_selection_menu():
    database_functions.clear_console()
    print("\nWould you like to:")
    print("1. Update your account name")
    print("2. Update your account pin")
    modification_user_select()

def admin_modification_selection_menu():
    database_functions.clear_console()
    print("\nWould you like to:")
    print("1. Update your account name")
    print("2. Update your account pin")
    print("3. Update a non-admin account name")
    print("4. Update a non-admin account pin")
    modification_admin_select()

def admin_log_in_selection_menu():
    database_functions.clear_console()
    print("\nWould you like to:")
    print("1. Create a new admin account")
    print("2. Delete an account")
    print("3. Update an account's information")
    print("4. Log Out")
    logIn_admin_select()

def logIn_user_select():
    while True:
        try:
            user_choice = int(input("\nEnter the number next to your choice (1-6): "))
        except ValueError:
            print("That's not a valid choice, please try again.")
        if user_choice == 1:
            database_functions.getBalance()
            break
        elif user_choice == 2:
            database_functions.deposit()
            break
        elif user_choice == 3:
            database_functions.widthdraw()
            break
        elif user_choice == 4:
            modification_selection_menu()
            break
        elif user_choice == 5:
            database_functions.delete_account()
            break
        elif user_choice == 6:
            database_functions.logOut()
            break
        else:
            database_functions.clear_console()

def home_user_select():
    av_choices = [1, 2, 3, 4]
    while True:
        user_choice = user_picker(av_choices)
        if user_choice == 1:
            database_functions.create_account("u")
        elif user_choice == 2:
            database_functions.logIn("u")
        elif user_choice == 3:
            database_functions.logIn("a")
        elif user_choice == 4:
            print("Thank you for using this banking system")
            exit()
        else:
            database_functions.clear_console()

def modification_user_select():
    while True:
        try:
            user_choice = int(input("\nEnter the number next to your choice (1 or 2): "))
        except ValueError:
            print("That's not a valid choice, try again.")

        if user_choice == 1:
            database_functions.modify_name("u")
            break
        elif user_choice == 2:
            database_functions.modify_pin("u")
            break

def modification_admin_select():
    while True:
        try:
            user_choice = int(input("\nEnter the number next to your choice (1-4): "))
        except ValueError:
            print("That's not a valid choice, try again.")
            continue

        if user_choice == 1:
            database_functions.modify_name("a", 0)
            break
        elif user_choice == 2:
            database_functions.modify_pin("a", 0)
            break
        elif user_choice == 3:
            database_functions.modify_name("u", 0)
            break
        elif user_choice == 4:
            database_functions.modify_pin("u", 0)
            break
        else: 
            print("That's not a valid choice, try again.")

def backToUserSignInMenu(typeAcc):
    if typeAcc == "u":
        user_log_in_selection_menu()
    elif typeAcc == "a":
        admin_log_in_selection_menu()

def logIn_admin_select():
    while True:
        try:
            user_choice = int(input("\nEnter the number next to your choice (1-4): "))
            break
        except ValueError:
            print("That is not a valid choice, please try again.")
        if user_choice == 1:
            database_functions.create_account("a")
        elif user_choice == 2:
            database_functions.delete_account("a")
        elif user_choice == 3:
            admin_modification_selection_menu()
        elif user_choice == 4:
            database_functions.logOut()
        else:
            print("That is not a valid choice, please try again.")

def user_picker(av_choices):
    while True:
        try:
            user_choice = int(input("\nEnter the number next to your choice (1 - 4): "))
        except ValueError:
            user_choice = None

        if user_choice not in av_choices or user_choice is None:
            print("That's not a valid choice, please try again.")
            continue
        return user_choice
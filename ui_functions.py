import database_functions

def user_selection_menu():
    database_functions.clear_console()
    print("\n--------------------------USER SELECTION--------------------------")
    print("\nWould you like to:")
    print("1. Create an Account")
    print("2. Log in")
    
def user_log_in_selection_menu():
    database_functions.clear_console()
    print("\n--------------------------USER SELECTION--------------------------")
    print("\nWould you like to:")
    print("1. Get balance")
    print("2. Make a deposit")
    print("3. Widthdraw from account")
    print("4. Update account information")

def modification_selection_menu():
    database_functions.clear_console()
    print("\n--------------------------USER SELECTION--------------------------")
    print("\nWould you like to:")
    print("1. Update your account name")
    print("2. Update your account pin")

def home_user_select():
    while True:
        try:
            user_choice = int(input("\nEnter the number next to your choice (1 or 2): "))
        except TypeError:
            print("That's not a valid choice, please try again.")

        if user_choice == 1:
            database_functions.create_account()
            break
        elif user_choice == 2:
            user_log_in_selection_menu()
            logIn_user_select()
            break
        else:
            database_functions.clear_console()
            print("That's not a valid choice, please try again.")

def logIn_user_select():
    while True:
        try:
            user_choice = int(input("\nEnter the number next to your choice (1-4): "))
        except TypeError:
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
        else:
            database_functions.clear_console()
            print("That's not a valid choice, please try again.")
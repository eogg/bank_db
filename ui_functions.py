import database_functions

#DISPLAYS HOME MENU
def home_selection_menu():
    database_functions.clear_console()
    print("\nWould you like to:")
    print("1. Create an Account")
    print("2. Log in")
    print("3. Log in as administrator")
    print("4. Exit baking system")
    home_select()

#ALLOWS FOR SELECTION FROM HOME MENU
def home_select():
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
            database_functions.clear_console()
            print("Thank you for using this banking system.")
            exit()
        else:
            database_functions.clear_console()


#DISPLAYS LOG_IN MENU, DEPENDING ON WHAT TYPE OF LOG IN WAS MADE USING {accType}
def log_in_selection_menu(accType):
    if(accType == "u"):
        database_functions.clear_console()
        print("\nWould you like to:")
        print("1. Get balance")
        print("2. Make a deposit")
        print("3. Withdraw from account")
        print("4. Update account information")
        print("5. Delete account")
        print("6. Log out")
        logIn_select(accType)
    else: 
        database_functions.clear_console()
        print("\nWould you like to:")
        print("1. Create a new admin account")
        print("2. Delete a user's account")
        print("3. Delete your account")
        print("4. Update an account's information")
        print("5. Log Out")
        logIn_select(accType)

#ALLOWS FOR SELECTION FROM LOG IN MENU USING {accType} TO FIGURE OUT WHAT TYPE OF ACCOUNT IS LOGGED IN
def logIn_select(accType):
    if(accType == "u"):
        av_choices = [1, 2, 3, 4, 5, 6]
        while True:
            user_choice = user_picker(av_choices)

            if user_choice == 1:
                database_functions.getBalance()
                break
            elif user_choice == 2:
                database_functions.deposit()
                break
            elif user_choice == 3:
                database_functions.withdraw()
                break
            elif user_choice == 4:
                modification_selection_menu("u")
                break
            elif user_choice == 5:
                database_functions.delete_account("u", 1)
                break
            elif user_choice == 6:
                database_functions.logOut()
                break
            else:
                database_functions.clear_console()
    else:
        av_choices = [1, 2, 3, 4, 5]
        while True:
            user_choice = user_picker(av_choices)

            if user_choice == 1:
                database_functions.create_account("a")
            elif user_choice == 2:
                database_functions.delete_account("a", 0)
            elif user_choice == 3:
                database_functions.delete_account("a", 1)
            elif user_choice == 4:
                modification_selection_menu(accType)
            elif user_choice == 5:
                database_functions.logOut()
            else:
                print("That is not a valid choice, please try again.")


#DISPLAYS ACCOUNT MODIFICATION MENU ACCORDING TO {accType}
def modification_selection_menu(accType):
    if(accType == "u"):
        database_functions.clear_console()
        print("\nWould you like to:")
        print("1. Update your account name")
        print("2. Update your account pin")
        print("3. Back")
        modification_select(accType)
    else:
        database_functions.clear_console()
        print("\nWould you like to:")
        print("1. Update your account name")
        print("2. Update your account pin")
        print("3. Update a non-admin account name")
        print("4. Update a non-admin account pin")
        print("5. Back")
        modification_select(accType)

#ALLOWS FOR SELECTION FROM ACCOUNT MODIFICATION MENY ACCORDING TO {accType}
def modification_select(accType):
    if(accType == "u"):
        av_choices = [1, 2, 3]
        while True:
            user_choice = user_picker(av_choices)

            if user_choice == 1:
                database_functions.modify_name("u", 1)
                break
            elif user_choice == 2:
                database_functions.modify_pin("u", 1)
                break
            elif user_choice == 3:
                backToUserSignInMenu("u")
            else: 
                print("That's not a valid choice, try again.")
    else:
        av_choices = [1, 2, 3, 4, 5]
        while True:
            user_choice = user_picker(av_choices)

            if user_choice == 1:
                database_functions.modify_name("a", 1)
                break
            elif user_choice == 2:
                database_functions.modify_pin("a", 1)
                break
            elif user_choice == 3:
                database_functions.modify_name("a", 0)
                break
            elif user_choice == 4:
                database_functions.modify_pin("a", 0)
                break
            elif user_choice == 5:
                backToUserSignInMenu("a")
            else: 
                print("That's not a valid choice, try again.")


#TAKES USER BACK TO SIGN IN MENU ACCORDING TO {typeAcc}
def backToUserSignInMenu(typeAcc):
    log_in_selection_menu(typeAcc)

#TAKES USER BACK TO UPDATE MENU ACCORDING TO {typeAcc}
def backToUpdateMenu(typeAcc):
    modification_selection_menu(typeAcc)

#FACILITATES THE USE OF PICKING THE OPTIONS FROM THE SELECTIONS.
def user_picker(av_choices):
    while True:
        try:
            user_choice = int(input("\nEnter the number next to your choice: "))
        except ValueError:
            user_choice = None

        if user_choice not in av_choices or user_choice is None:
            print("That's not a valid choice, please try again.")
            continue
        return user_choice
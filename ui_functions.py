import os
import mysql.connector
import database_functions
isActive = True

# def clear():
#     os.system('cls')
def clear():
    os.system("clear")

def user_selection_menu():
    clear()
    print("\n--------------------------USER SELECTION--------------------------")
    print("\nWould you like to:")
    print("1. Create an Account")
    print("2. Make a deposit")
    print("3. Withdraw from your account")
    print("4. Modify your account")

def modification_selection_menu():
    clear()
    print("\n--------------------------USER SELECTION--------------------------")
    print("\nWould you like to:")
    print("1. Update your account name")
    print("2. Update your account pin")

def user_select():
    while isActive:
        user_choice = int(input("\nEnter the number next to your choice (1-5): "));
        if user_choice == 1:
            database_functions.create_account()
            break
        elif user_choice == 2:
            database_functions.deposit()
            break
        elif user_choice == 3:
            database_functions.widthdraw()
            break
        # elif user_choice == 4:
        #     modification_selection_menu()
        #     break
        else:
            clear()
            print("That's not a valid choice, please try again.")
import os
import mysql.connector
import database_functions
isActive = True

def clear():
    os.system('cls')

def user_selection_menu():
    clear()
    print("\n--------------------------USER SELECTION--------------------------")
    print("\nWould you like to:")
    print("1. Create an Account")
    print("2. Make a deposit")
    print("3. Withdraw from your account")
    print("4. Modify your account")

def user_select():
    while isActive:
        user_choice = int(input("\nEnter the number next to your choice (1-5): "));
        if user_choice == 1:
            database_functions.create_account()
            break
        # elif user_choice == 2:
        #     display_Big_Mouth_Burgers_menu()
        #     big_mouth_burgers_selection()
        #     break
        # elif user_choice == 3:
        #     display_Ribs_and_Steaks()
        #     ribs_n_steaks_selection()
        #     break
        # elif user_choice == 4:
        #     display_Lunch_Specials()
        #     lunch_specials_selection()
        #     break
        # elif user_choice == 5:
        #     display_desserts()
        #     desserts_selection()
        #     break
        # else:
        #     print("That's not a valid choice, please try again.")



user_selection_menu()

user_select()
database_functions.printOutEntireTable()
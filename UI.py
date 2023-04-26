import ui_functions

while True:
    ui_functions.user_selection_menu()
    sure = str(input("Would you like keep going? y/n: "))
    if sure.lower() == "n":
        print("Thank you for using this banking app.")
        break
    elif sure.lower() == "y":
        continue
    else:
        print("That option is not valid, please try again.")
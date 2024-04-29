
#System packages

#External packages

#Import from functions.py
from functions import myhabits_htracker, template_htracker, database_htracker, stats_htracker

file_name = "myhabits.csv"

if (not os.path.isfile(file_name)):

print("Welcome to Habits Tracker\n")

def main_menu():
    print("1. My habits list")
    print("2. Templates")
    print("3. Habits database")
    print("4. View Statistics")
    print("5. Quit Application")
    
    user_selection = input("Enter your selection: ")
    return user_selection



selection = ""

while selection != "4":
    selection = main_menu()
    
    if (selection == "1"):
        myhabits_htracker()
    elif (selection == "2"):
        template_htracker()
    elif (selection == "3"):
        database_htracker()
    elif (selection == "4"):
        stats_htracker()
    elif (selection == "5"):
        print("you entered 5")
    else:
        print("Invalid option, please enter an option from 1-4")

print("Sad to see you go, see you next time!")
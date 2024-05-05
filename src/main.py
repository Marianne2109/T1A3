
#System packages
import csv
import os.path 

#External packages

#Import from functions.py
from functions import add_habits, edit_delete_log, activity_overview, habits_database

file_name = "habits.csv"

#Check of CSV exist and create one if it dooesn't 
if not os.path.isfile(file_name):
    with open (file_name, "w") as file:
        file.write("Habit Name, Start Date, Frequency, Mark Habit\n")



#Main function, run the application includes welcome message

print("Welcome to Habits Tracker\n")

#Main menu function, this is the main menu of the terminal application. 
#The user is prompted to enter input depending on what they wish to do.
def main_menu():
    print("Please choose from the menu below: \n")
    print("1. Add new habits") #user is asked to enter one or more habits to save 
    print("2. Edit, Delete or Mark habit") #Submenu
    print("3. Activity overview") #shows table with all saved habits
    print("4. Habits database") 
    #print("5. View Statistics")
    print("5. Quit Application")
    
user_selection = ""

#Main menu loop
while user_selection != 5:
    main_menu()   
    user_selection = int(input("Enter your choice from the menu number: \n")) 
    if user_selection == 1:
        add_habits(file_name) 
    elif user_selection == 2:
        edit_delete_log(file_name)
    elif user_selection == 3:
        activity_overview(file_name)
    elif user_selection == 4:
        habits_database()
    elif user_selection == 5:
        print("Are you leaving?")
    else:
        print("Invalid option, please try again by entering an option from 1-5")  
        

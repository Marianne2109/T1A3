
#System packages
import csv
import os.path 
import datetime as datetime


#External packages

#Import from functions.py
from functions import add_habits, edit_delete_log, activity_overview, habits_database


file_name = "habits.csv"


habits_database_file_path = "src/habits_database.csv"

#Check of CSV exist and create one if it dooesn't 
if not os.path.isfile(file_name):
    with open (file_name, "w") as file:
        file.write("Habit Name, Start Date, Frequency, Mark Habit\n")



print("\n\n-----Welcome to your Habits Tracker-----\n")

#Main menu function, this is the main menu of the terminal application. 
#The user is prompted to enter input depending on what they wish to do.
def main_menu():
    print("\n Please choose from the menu below: \n")
    print("1. Add new habits") #user is asked to enter one or more habits to save 
    print("2. Edit, Delete or Mark habit") #this option will display a submenu
    print("3. Activity overview") #shows table with all saved habits and the times it has been marked or logged as complete
    print("4. Habits database") #displays an inbuilt csv file as a table. This is to provide example of habits only.
    print("5. Quit Application") #break loop and exit application
    
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
        habits_database(habits_database_file_path)
    elif user_selection == 5:
        print("You are now leaving the application. See you next time!")
        break
    else:
        print("Invalid option, please try again by entering an option from 1-5")  
        

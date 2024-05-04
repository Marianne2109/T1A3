#System Packages
import csv
import datetime as dt

#External Packages
from prettytable import PrettyTable


print("\n           Welcome to your Habits Tracker \n")

#Main menu function, this is the main menu of the terminal application. 
#The user is prompted to enter input depending on what they wish to do.
def main_menu():
    print("Please choose from the menu below: \n")
    print("1. Create new habits") #user is asked to enter one or more habits to save 
    print("2. Edit, Delete or Mark habit") #Submenu
    print("3. Activity overview") #shows table with all saved habits
    print("4. Habits database")
    print("5. View Statistics")
    print("6. Quit Application")
    
user_selection = ""

while user_selection != 6:
    main_menu()   
    user_selection = int(input("Enter your choice from the menu number: \n")) 
    if user_selection == 1:
        create_new_habit() 
    elif user_selection == 2:
        edit_delete_log()
    elif user_selection == 3:
        activity_overview()
    elif user_selection == 4:
        habits_database()
    elif user_selection == 5:
        view_statistics()
    elif user_selection == 6:
        print("Are you leaving?")
    else:
        print("Invalid option, please try again by entering an option from 1-5")  
        
file_name = [habits_database.csv, create_new.csv]

def create_new_habit(file_name):
    print("Now let's start tracking some habits!\n")
#first create CSV file
    create_new = open(file_name, "w") as file:
#add one or more habits to CSV file
#habits variables for habit name, start date and frequency (daily or weekly)

def edit_delete_log(file_name):
#submenu that will give the option to edit, delete or mark a habit as completed

def activity_overview(file_name):
#This function will display all saved habits in a table (habit name and start date)

def habits_database():
#This function will display a csv file with a list of random habits that can be tracked as reference
#It will have the option to add habit to the list for future reference 

def view_stats():
#This function will display a list of all habits and their streak
#User can check the stats for individual habits. 
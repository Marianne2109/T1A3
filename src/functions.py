#System Packages
import csv
import os 
import datetime as datetime

#External Packages
from prettytable import PrettyTable


#print("\n           Welcome to your Habits Tracker \n")



#Function to create CSV file is it dooesn't exist
def create_new(file_name):
 if (not os.path.isfile(file_name)):
    print("File not found, creating new file")
    create_new = open(file_name, "w")
    create_new.write("habit name", "start date", "frequency", "mark habit")
    create_new.close()
    
file_name = []



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
        create_new(file_name) 
    elif user_selection == 2:
        edit_delete_log(file_name)
    elif user_selection == 3:
        activity_overview(file_name)
    elif user_selection == 4:
        habits_database(file_name)
    elif user_selection == 5:
        view_statistics()
    elif user_selection == 6:
        print("Are you leaving?")
    else:
        print("Invalid option, please try again by entering an option from 1-5")  
        
file_name = [habits_database.csv, create_new.csv]


def create_new(file_name):
    print("Now let's start tracking some habits!\n")
    with open(create_new, "a") as file:
       writer = csv.writer(file) 
       writer.writerow = (["habit name", "start date", "frequency", "mark habit"])
       #habits_number = int(input("Please enter how many habits would you like to add: "))
        habitname = input("Enter a habit you would like to start tracking: ")
        print("You can log this activity daily, weekly or monthly, it's up to you!")
        frequency = input("How often would you like to log this activity: ")
           
        
#add one or more habits to CSV file
#habits variables for habit name, start date and frequency (daily or weekly)

def edit_delete_log():
    print("edit, delete or log a habit")
#submenu that will give the option to edit, delete or mark a habit as completed

def activity_overview():
    print("print table with current habits")
#This function will display all saved habits in a table (habit name and start date)

def habits_database(habits_database):
    print("see list of habit for inspiration")
#This function will display a csv file with a list of random habits that can be tracked as reference
#It will have the option to add habit to the list for future reference 

def view_stats():
    print("view statisics")
#This function will display a list of all habits and their streak
#User can check the stats for individual habits. 
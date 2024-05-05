#System Packages
import csv
import os.path 
import datetime as datetime

#External Packages
from prettytable import PrettyTable


#Function to create a new habit and append to the CSV file
def add_habits(file_name):
    print("\n Let's start tracking some habits!\n")
    
    #User to input name of a habit 
    habit_name = input("Enter a habit you would like to start tracking: ")
    
    #User to set a date to start tracking
    while True:
        try:  
            start_date = input("Enter the date you'd like to start tracking this habit (YYYY/MM/DD): ")
            date = datetime.date.strptime(start_date, format="%Y/%m/%d").date()     
        except ValueError:
            print("Invalid date format. Please enter a valid date (YYYY/MM/DD)")
            continue
        else:
            break
    
    #User set to specify the frequency they want to check the habit
    while True:
        frequency = input("How often would you like to mark this activity (daily or weekly): ")
        if frequency not in ["daily", "weekly"]:
            print("Invalid input. Please enter 'daily' or 'weekly'")
            continue
        else:
            break
    
    #Append habits to CSV file
    with open(file_name, "a") as f:
        writer = csv.writer(f) 
        writer.writerow = ([habit_name, start_date, frequency, False])
        
    
       
        

#submenu that will give the option to edit, delete or mark a habit as completed
def edit_delete_log():
    print("edit, delete or log a habit")


def activity_overview():
    print("print table with current habits")
    
#This function will display all saved habits in a table (habit name and start date)

def habits_database(habits_database):
    print("see list of habit for inspiration")
    #with open(habits_database, "r") as file:
#This function will display a csv file with a list of random habits that can be tracked as reference
#It will have the option to add habit to the list for future reference 

#def view_stats():
    #print("view statisics")
#This function will display a list of all habits and their streak
#User can check the stats for individual habits. 
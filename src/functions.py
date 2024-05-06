#System Packages
import csv
import os.path 
import datetime as datetime

#External Packages
from prettytable import PrettyTable

file_name = "habits.csv"


#Function to create a new habit and append to the CSV file
def add_habits(file_name):
    print("\n Let's start tracking some habits!\n")
    
    #User to input name of a habit 
    habit_name = input("Enter a habit you would like to start tracking: ")
    
    #User to set a date to start tracking
    while True:
        start_date = input("Enter the date you'd like to start tracking this habit (YYYY/MM/DD): ")
        try:   
            date_string = datetime.datetime.strptime(start_date, "%Y/%m/%d").date()     
        except ValueError:
            print("Invalid date format. Please enter a valid date (YYYY/MM/DD)")
            continue
        else:
            break
    
    #User set to specify the frequency they want to check the habit
    while True:
        frequency = input("How often would you like to mark this activity (daily or weekly): ")
        print("\n >>> Your Habit has been saved, you are now ready to start tracking! <<<")  
        print(">>> You can record a habit as complete from the menu '2. Edit, Delete or Mark habit' <<<")     
        if frequency not in ["daily", "weekly"]:
            print("Invalid input. Please enter 'daily' or 'weekly'")
            continue
        else:
            break
    
    #Append habits to CSV file
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f) 
        writer.writerow([habit_name, start_date, frequency, ""])
        
#Function to check if a habit already exist in the CSV file

#Function to read habits.csv data
def read_habits_csv(file_name):
    habits_list = []
    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            habits_list.append(row)
    return habits_list


#Function for submenu that will give the option to edit, delete or mark a habit as completed
def edit_delete_log(file_name):
    print("Select an option from below to edit, delete or log a habit: \n")
    while True:
        print("1. Edit an existing habit")
        print("2. Delete an existing habit")
        print("3. Mark a complete habit")
        print("4. Return to Main menu")
    
        user_selection = int(input("Enter your choice: "))
        
        if user_selection == 1:
            print("You selected the option to Edit an existing habit")
        elif user_selection ==2:
            print("You selectec the option to Delete an existing habit")
        elif user_selection ==3:
            mark_habit(file_name)
        elif user_selection ==4:
            print("Exit Submenu \n\n")
            break
        else:
            print("Invalid option. Please try again by entering an option from 1-4")
        
#Function to mark a habit when completed and save marked habits to csv file   
def mark_habit(file_name):
    habit_name = input("Which habit would you like to mark as complete?: ")
    habit_list = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (habit_name != row [0]):
                habit_list.append(row)
            else:
                if str(datetime.now()).split(" ")[0] != row[-1]:
                    habit_list.append([row[0], row[1], row[2], int(row[3]) + 1, str(datetime.now()).split(" ")[0]])
                else:
                    habit_list.append(row)
                    print("You have already marked this habit today")
    
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerows(habit_list)
    

#Function to print the data from the habits.csv file as a table. The table will display the habit column and marked columm 
#it will serve as a visual input for how habit are tracking.
def activity_overview(file_name):
    print("See the table below for all your current habits")
    table = PrettyTable()
    table.field_names = ["Habit", "Log"]
    with open("habits.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            table.add_row([row[0], row[3]])         
    print(table)
    


def habits_database(habits_database):
    print("See list of habits to get some ideas of what you can track")
    print("You can add more habit to this list so you can remember in the future")    
    table= PrettyTable()
    with open (habits_database, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            table.add_row([row[0]])
    print(table)
            
        
    #with open(habits_database, "r") as file:
#This function will display a csv file with a list of random habits that can be tracked as reference
#It will have the option to add habit to the list for future reference 


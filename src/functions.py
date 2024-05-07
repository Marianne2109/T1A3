#System Packages
import csv
import os.path 
import datetime as datetime

#External Packages
from prettytable import PrettyTable

file_name = "habits.csv"
habits_database_file_path = "src/habits_database.csv".lower()


#Function to create a new habit and append to the CSV file
def add_habits(file_name):
    print("\n Let's start tracking some habits!\n")
    
    #User to input name of a habit 
    habit_name = input("Enter a habit you would like to start tracking: ").lower()
    
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
        frequency = input("How often would you like to mark this activity (daily or weekly): ").lower()
        print("\n >>> Your Habit has been saved, you are now ready to start tracking! <<<")  
        print(">>> You can record a habit as complete from the menu '2. Edit, Delete or Mark habit' <<<")     
        if frequency not in ["daily", "weekly"]:
            print("Invalid input. Please enter 'daily' or 'weekly'")
            continue
        else:
            break
    
    #Append habits to CSV file
    with open(file_name, "a") as f:
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
            edit_habit(file_name)
        elif user_selection ==2:
            delete_habit(file_name)
        elif user_selection ==3:
            mark_habit(file_name)
        elif user_selection ==4:
            print("Exit Submenu \n\n")
            break
        else:
            print("Invalid option. Please try again by entering an option from 1-4")

def edit_habit(file_name):
    habit_name = input("What habit would you like to edit?: ").lower()
    print("Now, enter the new details for this habit: \n")    
    new_habit_name = input("Enter the new name: ").lower()    
    new_start_date = input("Enter the new start date (YYYY/MM/DD): ")    
    new_frequency = input("Enter the new frequency for this habit 'daily' or 'weekly': ").lower()
    habit_list = []
    
    with open (file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            habit_list.append(row)
    
    #Write edited habits to CSV file
    with open(file_name, "w") as f:
        writer = csv.writer(f) 
        writer.writerow([habit_list])
    
    for habit in habit_list:
        if habit[0] == habit_name:
            habit[0] = new_habit_name
            habit[1] = new_start_date
            habit[2] = new_frequency
        else:
            break
    
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(habit_list)
            
    
    
#Function to delete a habit. This will delete the row completely because it's based on the habit_name.
#It'll iterate through the rows until a matching row and then remove that row.
def delete_habit(file_name, habit_name):
    habit_name = input("Type in the habit that you'd like to delete: ").lower()
    rows = []
    with open (file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != habit_name:
                rows.append(row)
                
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
      
        
#Function to mark a habit when completed and save marked habits to csv file   
def mark_habit(file_name):
    habit_name = input("Which habit would you like to mark as complete?: ").lower()
    habit_list = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if  habit_name != row [0].lower():
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
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            table.add_row([row[0], row[3]])         
    print(table)
    

#Function to print a table with a number of habits that can be tracked. This CSV comes with the program and the user can 
#use as a reference for habits that can be tracked.
def habits_database(habits_database_file_path):
    print("See list of habits to get some ideas of what you can track")  
    table= PrettyTable()
    with open (habits_database_file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            table.add_row([row[0 - 1]])
    print(table)

        
        


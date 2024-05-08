#System Packages
import csv
import os.path 
import datetime as datetime

#External Packages
from prettytable import PrettyTable

#Global Variables
file_name = "habits.csv"
habits_database_file_path = "src/habits_database.csv".lower()

#General error handling function
def handle_error(exception):
    print("Oops! It looks like something went wrong. Please try again.")

#Function to create a new habit and append to the CSV file
#User will be prompted to enter a habit name, date to start tracking and frequency they wish to record the habit.
def add_habits(file_name):
    print("\n Let's start tracking some habits!\n")
    try:
        habit_name = input("Enter a habit you would like to start tracking: ").lower()
        
        existing_habits = read_habits_csv(file_name)
        for row in existing_habits:
            if habit_name == row[0].lower():
                print("This habit has already been created. Please enter a different habit.")
                return
            
        while True:
            start_date = input("Enter the date you'd like to start tracking this habit (YYYY/MM/DD): ")
            try:   
                date_string = datetime.datetime.strptime(start_date, "%Y/%m/%d").date()     
            except ValueError:
                print("Invalid date format. Please enter a valid date (YYYY/MM/DD)")
                continue
            else:
                break
    
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
    except Exception:
        handle_error
        

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
    print("Select an option from the menu below to edit, delete or log a habit: \n")
    try:
        while True:
            print("1. Edit an existing habit")
            print("2. Delete an existing habit")
            print("3. Mark a completed habit")
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
    except Exception:
        handle_error
            
#Function to edit a habit and the update the changes in the CSV file
def edit_habit(file_name):
    habit_name = input("What habit would you like to edit?: ").lower()
    habit_list = []
     
    try:
        with open (file_name, "r") as f:
            reader = csv.reader(f)
            habit_list = list(reader)
    
        index = None
        for i, row in enumerate(habit_list):
            if row[0].lower() == habit_name:
                index = i
                break
 
        if index is not None: 
            new_habit_name = input("Enter the new habit name: ").lower()    
            new_start_date = input("Enter the new start date (YYYY/MM/DD): ")    
            new_frequency = input("Enter the new frequency for this habit 'daily' or 'weekly': ").lower()
        
            habit_list[index] = [new_habit_name, new_start_date, new_frequency, ""]
       
    #Write edited habits back to CSV file
            with open(file_name, "w") as f:
                writer = csv.writer(f) 
                writer.writerows(habit_list)
                
            print("Habit updated successfully!")
        else:
            print("Habit not found.")
    except Exception:
        handle_error 
            
    
    
#Function to delete a habit. This will delete the row completely because it's based on the habit_name.
#It'll iterate through the rows until a matching row and then remove that row.
def delete_habit(file_name):
    habit_name = input("Type in the habit that you want to delete: ").lower()
    rows = []
    try:
        with open (file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != habit_name:
                    rows.append(row)
                
        with open(file_name, "w") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
            print("The habit has been successfully deleted \n")
    except Exception:
        handle_error
      
        
#Function to mark a habit when it has been completed and save marked habits to csv file.
#it will not changed habit_name, date_start or frequency. It will add an incrementing count for each time that the habit is recorded.  
def mark_habit(file_name):
    habit_name = input("Which habit would you like to mark as complete?: ").lower()
    habit_list = []
    habit_found = False
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if  (habit_name != row [0].lower()):
                    habit_list.append(row)
                else:
                    habit_found = True
                    if str(datetime.datetime.now()).split(" ")[0] != row[-1]:
                        count = int(row[3]) + 1 if row[3] else 1
                        row[3] = str(count)
                        row[-1] = str(datetime.datetime.now()).split(" ")[0] 
                        habit_list.append(row)
                        print(f"Habit '{habit_name}' marked as completed. New log: {row}")    
                    else:
                        print("You have already marked this habit today")
                    continue
                
        if not habit_found:
            print(f"Sorry,'{habit_name}' does not exist.")
            return
        
        with open(file_name, "w") as f:
            writer = csv.writer(f)
            writer.writerows(habit_list)
    except Exception:
       handle_error
    

#Function to print the data from the habits.csv file as a table. The table will display the habit column and marked columm 
#it will serve as a visual input for how habit are tracking.
def activity_overview(file_name):
    print("See the table below for all your current habits")
    table = PrettyTable()
    table.field_names = ["Habit", "Log"]
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                table.add_row([row[0], row[3]])         
        print(table)
    except Exception:
        handle_error

#Function to print a table with names of habits that can be tracked. This CSV comes with the program to provide examples only.
def habits_database(habits_database_file_path):
    print("See list of habits to get some ideas of what you can track")  
    table= PrettyTable()
    table.field_names = ["Habits reference list"]
    try:
        with open (habits_database_file_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                table.add_row([row[0]])
        print(table)
    except Exception:
        handle_error
        
        


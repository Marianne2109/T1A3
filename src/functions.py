
#System packages
import csv
import os.path


#External packages
from prettytable import PrettyTable


# Define file path to files used in the application



habits_database_file_path = "./src/habits_database.csv"
habits_database_header = "habit_name,habit_log"


#Create new list options, make a new list of habits to track
#enter habit, frequency for tracking and log habit when done
create_new_habit = {
    "Create a new list of habits": 
     
}

#My habits list, list of the habits currently being tracked in a table. Log a habit by entering 0 (zero)
#Option to add or delete habits from the list. 
my_habits_list = {
    "View current tracked habits": "display_records('entry', )",
    "Add habit or log to current list": "add_log_submenu('log', )", 
    "Delete habit or log from current list": "delete_log_submenu('delete', )", 
}

#Habit database options, view the current database of habit that can be tracked
#as a reference point. Add or delete habits.
habits_database = {
    "View Habits in database": "habits_database(habits_database_file_path)",
    "Add new habit to the database": "add_submenu('habit', habits_database_file_path)",
    "Delete habit": "delete_submenu('habit', habits_database_file_path, habits_database_header)",
}


#View statistics, options to analise the performance of currents tracked habits
view_statistics = {
    
}



#Main menu function, to navigate through the general options in the menu
def main_menu():
    print("Please choose from the menu below: \n")
    print("1. Create habit")
    print("2. My current habits")
    print("3. Habits database")
    print("4. View Statistics")
    print("5. Quit Application")
    
    
user_selection = ""

while user_selection != 5:
    main_menu()   
    user_selection = int(input("Enter your choice from the menu number: \n")) 
    if user_selection == 1:
        create_new_habit() 
    elif user_selection == 2:
        my_habits_list()
    elif user_selection == 3:
        habits_database()
    elif user_selection == 4:
        view_statistics()
    elif user_selection == 5:
        print("Are you leaving?")
    else:
        print("Invalid option, please try again by entering an option from 1-5")  


#Function to check if a CSV file exists
file_name = "newhabits.csv"

if (not os.path.isfile(file_name)):
    

#Create new habit, this function is to create a new habit to start tracking,
#the new habit will start a new habits list or be appended to an existing habits list
#habit:habit name
#frequency: daily, weekly, fortnightly, monthly
#mark the date to start tracking. 
#log: use 0 (zero) to log a habit when it's done
def create_new_habit(newhabits.csv):
    print("You can check the 'Habits Database' for ideas of habits you can start tracking today")
    with open ("newhabits.csv", "w+") as file:
       newhabits = csv.writer(file) 
       newhabits.writerow = (["habit", "frequency", "done"])
       habitsnumber = int(input("Please enter how many habits would you like to add: "))
       for i in range (habitsnumber):
           habitname = input("Habit " + str(i+1)" : Enter a habit you would like to start tracking: ")
           print("You can log this activity daily, weekly or monthly, it's up to you!")
           frequency = input("Habit " + str(i+1)" : How often would you like to log this activity: ")
           done = input("Habit " + str(i+1)"  : If you have completed this, log by entering 0: ")
            
  
    
    
    #create_new_list_file = open("habits_database.csv", "r+")
   # create_new_list_file.write("habit,frequency")
    #create_new_list_file.close()

def my_habits_list():
    print("Here is a list of the habits you are currently tracking\n")

#Database, function to display habits listed in the Database
def habits_database (csv_path):
    with open ("habits_database.csv", "r") as file:
        csvreader = csv.reader(file)
        header = next (csvreader)
        habits_table = PrettyTable()
        habits_table.field_name = ["habit", "log"]
        for row in csvreader:
            (
                habit_name,
                habit_log,
            ) = row
            habits_table.add_row(row)
        print("See the current habits stored in the database: \n")
        print("habits_table\n")
        input("Press enter to return to the main menu")
        

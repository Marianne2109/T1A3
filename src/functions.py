
import csv

#External packages
from prettytable import PrettyTable


# Define file path to files used in the application



habits_database_file_path = "./src/habits_database.csv"
habits_database_header = "habit_name,habit_log"


#Create new list options, make a new list of habits to track
#enter habit, frequency for tracking and log habit when done
create_new_list = {
    "Create New habits list": "create_submenu('new', new_habits_file_path)"       
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
    print("1. Create new list")
    print("2. My habits list")
    print("3. Habits database")
    print("4. View Statistics")
    print("5. Quit Application")
    
    
user_selection = ""

while user_selection != 5:
    main_menu()   
    user_selection = int(input("Enter your choice from the menu number: \n")) 
    if user_selection == 1:
        create_new_list() 
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



#Create new list, this function is to display option for a new habits list
#habit:habit name
#frequency: daily, weekly, fortnightly, monthly
#log: use 0 (zero) to log a habit when it's done
def create_new_list(habit, frequency, log):
    habit_list = {"habit": habit, "frequency": frequency, "log": log}
    print("Ready to start? Let's create a new List of Habits to track!\n\n")
    print("You can check the 'Habits Database' for ideas of habits you can start tracking today")
    add_new_list.append(habit_list)
    add_new_list = input("What habit would you like to start tracking? Please enter: ")
    
    
    #create_new_list_file = open("habits_database.csv", "r+")
   # create_new_list_file.write("habit,frequency")
    #create_new_list_file.close()

def my_habits_list():
    print("Here is the list of the habits you are currently tracking\n")

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
        

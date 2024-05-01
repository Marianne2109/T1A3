
import csv

# Define file path to files used in the application



habits_database_file_path = "src/habits_database.csv"
habits_database_header = "habit_name,habit_log"


#Main menu function, to navigate through the general options in the menu
def main_menu():
    print("Please choose from the menu below: \n")
    print("1. Create new list")
    print("2. My habits list")
    print("3. Habits database")
    print("4. View Statistics")
    print("5. Quit Application")
    
    user_selection = int(input("Select an option by entering the menu number: "))
    return user_selection

user_selection = ""

while user_selection != 5:
    user_selection = main_menu()    
    if (user_selection == 1):
        create_new_list() 
    elif (user_selection == 2):
        my_habits_list()
    elif (user_selection == 3):
        habits_database()
    elif (user_selection == 4):
        view_statistics()
    elif (user_selection == 5):
        print("Are you leaving?")
    else:
        print("Invalid option, please enter an option from 1-5")

print("Sad to see you go, see you next time!")


#Create new list, create function to display option for a new habits list
def create_new_list(habit, frequency, log):
    habit_list = {"habit": habit, "frequency": frequency, "log": log}
    print("Let's create a new List of Habits to track!\n")
    add_new_list.append(habit_list)
    add_new_list = input("What habit would you like to start tracking? Please enter: ")
    
    
    #create_new_list_file = open("habits_database.csv", "r+")
   # create_new_list_file.write("habit,frequency")
    #create_new_list_file.close()

def my_habits_list():
    print("Here is the list of the habits you are tracking\n")

#Database, function to display habits listed in the Database
def habits_database(csv_path):

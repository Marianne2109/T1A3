

#Main menu function, to navigate through the general options in the menu
def main_menu():
    print("Select an option:\n 1. My habits list")
    print("2. Create new list")
    print("3. Habits database")
    print("4. View Statistics")
    print("5. Quit Application")
    
    user_selection = int(input("Enter your selection: "))
    return user_selection

user_selection = ""

while user_selection != 5:
    user_selection = main_menu()
    
    if (user_selection == 1):
        my_habits_list()
    elif (user_selection == 2):
        create_new_list()
    elif (user_selection == 3):
        habits_database()
    elif (user_selection == 4):
        view_statistics()
    elif (user_selection == 5):
        print("Are you leaving?")
    else:
        print("Invalid option, please enter an option from 1-5")

print("Sad to see you go, see you next time!")

#Function 

#file_name = "myhabits.csv"

# if the file doesn't exist
#if (not os.path.isfile(file_name)):
    # create file
    #myhabits_file = open(file_name, "w")
    # enter info(headings) into the file
    #myhabits_file.write("habit,log")



#def myhabits_htracker():
    print("My habits list")

##def template_htracker():
    #print("Templates options")
    
#def database_htracker():
    #print("Habits Database")

#def stats_htracker():
    #print("stats")
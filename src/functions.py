
file_name = "myhabits.csv"

# if the file doesn't exist
if (not os.path.isfile(file_name)):
    # create file
    myhabits_file = open(file_name, "w")
    # enter info(headings) into the file
    myhabits_file.write("habit,log")



def myhabits_htracker():
    print("My habits list")

def template_htracker():
    print("Templates options")
    
def database_htracker():
    print("Habits Database")

def stats_htracker():
    print("stats")
    
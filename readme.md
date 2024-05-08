# Terminal Application
## Content
1. Links
2. Help Documentation
3. Code style guide
4. Features and Functionality
5. Implementation Plan
6. Testing
7. References

## Links
- GitHub repo:
- Trello board:

## Help Documentation
### Dependencies and download:
* You will need to have Pyhon3 installed. You can check if Python3 is installed by opening the terminal and entering `python3 –version`. If python is not installed, go to the oficial website to download. 
* Other dependencies will be installed by virtual environment - see installation
* Download the ZIP file from the source repository. Then open/unzip file.

### Installation:
* Open a standalone terminal from the command line. 
* Clone the GitHub repository from SSH or HTTPS<br>
  - Via SSH:<br>
  `git@github.com:Marianne2109/T1A3.git`

  - Via HTTPS:<br>
  `https://github.com/Marianne2109/T1A3.git`

* From current location navigate to `/src` directory in the cloned repository<br>
       `cd T1A3-TerminalApplication/src`

* Enter `./run.sh` to set up the virtual environment and run the application. 

* If you encounter issues try enter `chmod +x run.sh` then enter `./run.sh` again.

* The rest of the dependencies should be installed by the program. 

###### Welcome to the application. The app will now guide the user through the options available in the main menu, moving to the submenu accordingly.

## Code style guide
The code for this application was written using [PEP 8 - Style Guide for Python](https://peps.python.org/pep-0008/) 

## Features and Functionality
There are five features including the main menu and three other features from a ‘submenu’. 
**Main Menu:** <br> 
The main menu is displayed when the application is successfully installed. The other features can be accessed from the main menu loop. 
The menu options are displayed and the user is prompted to select an option from the main menu. The user input will display the corresponding function, or elif it will gracefully quit the application; else the output will indicate to try again.

**Add new habits:** <br> 
This is the Option 1 from the main menu. The purpose of this function is to allow the user to add new habits to a CSV file. 
To check if the CSV file exists there is a code block at the start of main.py. The `os.path.isfile()` function uses the `os.path` module to check if the file already exists; if the file does not exist then it’s created so the habits can be saved to that file. 
The `add_habit()` feature is wrapped in a try-except block used for error handling.
The code prompts the user to input a habit name after which the `read_habits_csv()` function iterates through the rows in the saved csv file to check if the user input (habit) already exists. ‘
Next the code prompts the user to enter a start date for tracking the habit in “YYYY/MM/DD”. The date is validated using try-except until the input is a valid date.
The code moves to the frequency at which they want to track the habit (daily or weekly).
Then using the csv.writer object, the file is open in append mode so the data is added without rewriting over any potential existing habits. 

**Edit, Delete or Mark habits:** <br>
This is option 2 from the main menu. This function displays a submenu, explained below. 
The function uses a while loop so the user is asked for input until they select the option to return to the main menu. 
The user selection will then call one of the following functions:
 * Edit a habit:
 * Delete a habit:
 * Mark a habit:
   
**Activity overview:**

**Habits Database:**

## Implementation Plan
## Testing
## References




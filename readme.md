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
- [Trello board](https://trello.com/b/1KoC9qTa/t1a3-terminalapplication)

## Help Documentation
### Dependencies and download:
* You will need to have Pyhon3 installed. You can check if Python3 is installed by opening the terminal and entering ```python3 –version```. If python is not installed, go to the oficial website to download. 
* Other dependencies will be installed by virtual environment - see installation
  * The external package used is `PrettyTable` 3.10.0
* Download the ZIP file from the source repository. Then open/unzip file.

### Installation:
* Open a standalone terminal from the command line. 

* Clone the GitHub repository from SSH or HTTPS<br>
  - Via SSH:<br>
  ```git clone git@github.com:Marianne2109/T1A3.git```

  - Via HTTPS:<br>
  ```git clone https://github.com/Marianne2109/T1A3.git```

* From current location navigate to `/src` directory in the cloned repository<br>
  ```cd T1A3-TerminalApplication/src```

* To set up the virtual environment and run the application, enter: <br>
  ```./run.sh```

* If you encounter issues try entering: <br>
  ```chmod +x run.sh``` 
  then enter again <br>
  ```./run.sh```

* The rest of the dependencies should be installed by the program. 

###### Welcome to the application. The app will now guide the user through the options available in the main menu, moving to the submenu accordingly.

## Code style guide
The code for this application was written using [PEP 8 - Style Guide for Python](https://peps.python.org/pep-0008/) 
PEP 8 is the official style guide for Python code. Some key points include:
* Indentention: Use 4 spaces per indentention level.
* Line lenght of maximum 79 characters.
* Avoid extraneous whitespace immediately inside parenthesis, brackets or braces; before comma, semicolon or colon.
* Use of `CamelCase` and `lowercase_with_underscore` for variable names.
Following PEP 8 ensures that the code is consistent and easy to read.

## Features and Functionality
There are five features including the main menu and three other features from a ‘submenu’. <br>
* **Main Menu:** <br> 
The main menu is displayed when the application is successfully installed. The other features can be accessed from the main menu loop. 
The menu options are displayed and the user is prompted to select an option from the main menu. The user input will display the corresponding function, or elif it will gracefully quit the application; else the output will indicate to try again.

* **Add new habits:** <br> 
This is the Option 1 from the main menu. The purpose of this function is to allow the user to add new habits to a CSV file. 
To check if the CSV file exists there is a code block at the start of main.py. The `os.path.isfile()` function uses the `os.path` module to check if the file already exists; if the file does not exist then it’s created so the habits can be saved to that file. 
The `add_habit()` feature is wrapped in a try-except block used for error handling.
The code prompts the user to input a habit name after which the `read_habits_csv()` function iterates through the rows in the saved csv file to check if the user input (habit) already exists. ‘
Next the code prompts the user to enter a start date for tracking the habit in “YYYY/MM/DD”. The date is validated using try-except until the input is a valid date.
The code moves to the frequency at which they want to track the habit (daily or weekly).
Then using the csv.writer object, the file is open in append mode so the data is added without rewriting over any potential existing habits. 

* **Edit, Delete or Mark habits:** <br>
This is option 2 from the main menu. This function displays a submenu, explained below. 
The function uses a while loop so the user is asked for input until they select the option to return to the main menu. 
The user selection will call one of the functions within the submenu. Each function considers potential errors with try-except and also calls a `handle_error` function. The options for the submenu are explained next:
 * Edit a habit:<br>
Edit habit is the submenu option 1. Allows the user to edit an existing habit
The function `edit_habit(file_name)` calls for the variable `file_name`, reads the existing habits from the CSV and updates the details if the habit is found. Then writes the updates to the csv file.

 * Delete a habit:<br>
From the submenu option 2, this function allows the user to delete an existing habit. The function reads the CSV file, removes the row and then updates the csv file

 * Mark a habit:<br>
From submenu option 3. This function prompts the user to enter a habit they wish to mark off as complete. The habit can be marked once per day. Using the datetime package, `datetime.now()` it creates a stamp of the current date so the habit can be marked once per day.  After the habit is marked the function includes an incrementing count for a specific habit to be stored in the fourth column (row [3]) of the csv file The changes are then written back to the csv file. 
   
* **Activity overview:** <br>
	This is option 3 from the main menu. The function `activity_overview()` displays all saved habits and their corresponding logs presenting the data structured as a table. Using the PrettyTable library the data is structured and formatted to present the information as a table. This can be used to analyse the habits further, though a statistics module was not included in the current application. My intention is for the `activity_overview()` function to provide the user with a way of analysing the habits performance. For this reason, only the first column (row 0) and the fourth column (row 3) are displayed in the PrettyTable.
After the rows have been added, using the `print()` function the data is displayed as a table.
The function is wrapped in a try-except block for ErrorHandling.

* **Habits Database:** <br>
This is option 4 from the main menu. The purpose of this function is to serve as a reference for users to see examples of habits and help with ideas of habits they can track. The data is displayed as a table to make it visually appealing. It uses the csv.reader to read the data from a predefined csv file. The data is passed to PrettyTable printed as a table using the function `print()`. 


## Implementation Plan
The implementation plan included an analysis of the feautures  of the application and feasibility for me at my current level to  be able to achieve my plan. 
This included the use of pseudocode and implementation of a Trello board (link provided) where I created cards and checklists for each feature of the application. The card included a deadline date. I was behind in many areas but having the board was of tremendous help for accountability and efficiency. 

## Testing

## References
* Python datetime module 2019, GeeksforGeeks, viewed May 2024, <https://www.geeksforgeeks.org/python-datetime-module/>.
* Steps to Write and Execute a Shell Script - javatpoint n.d., www.javatpoint.com, viewed May 2024, <https://www.javatpoint.com/steps-to-write-and-execute-a-shell-script>.
* van Rossum, G, Warsaw, B & Coghlan, N 2001, PEP 8 – Style Guide for Python Code, peps.python.org, viewed May 2024, <https://peps.python.org/pep-0008/>.





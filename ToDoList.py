# ------------------------------------------------------------------------ #
# Title: The To Do List Script (Assignment05)
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# CBridge,11.12.2022,Added missing code to script to complete Assignment05
# CBridge,11.14.2022,Added comments and updated Step 6 to save the file
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
strTask = ""    # Capture a new task from the user
strPriority = ""    # Capture the task's priority from the user

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

try:
    objFile = open(strFile, "r")                                    # open ToDoList.txt in read mode
    for row in objFile:
        strData = row.split(",")
        dicRow = {"Task": strData[0], "Priority": strData[1].strip()}   # convert strData to dictionary (dicRow)
        lstTable.append(dicRow)                                     # add dicRow to the list table
    objFile.close()
except:                                                 # Provide user-friendly message of ToDoList.txt does not exist
    print("No To Do list created yet. Try adding some tasks!")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("Task" + "," + "Priority")                                # create a simple header
        for row in lstTable:
            print(row["Task"] + "," + row["Priority"])                  # print each task and priority on a new line
            continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("Add a Task: ")
        strPriority = input("What is the Priority (low/medium/high)? ")
        dicRow = {"Task": strTask, "Priority": strPriority}             # add the new task and priority to dicRow
        lstTable.append(dicRow)                                         # append dicRow to the list table (lstTable)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        if lstTable:
            strTask = input("Which task should be removed? ")
            for row in lstTable:                                            # remove user-specified task if it exists
                if row["Task"].lower() == strTask.lower():
                    lstTable.remove(row)
                    print(strTask.title() + " has been removed.")
        else:                                                               # notify user task provided does not exist
            print(f"{strTask.title()} is not on your to do list.")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(strFile, "w")                              # open file in write mode
        for item in lstTable:
            objFile.write(item["Task"] + "," + item["Priority"] + "\n")  # write lstTable items to file
        objFile.close()
        print("Data Saved!")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Time to get to work on your To Do list!")                # provide user motivational message before exit
        break  # and Exit the program

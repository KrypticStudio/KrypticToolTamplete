### Kryptic Studio ###

# Local Libraries
from Core import version
# Libraries

# Standard Libraries
import os
import time


# check whether user is root
#if os.geteuid() != 0:
#    print("\nERROR: Kryptic Hacking Tools must be run with root privileges. Try again with sudo: sudo python3 KrypticHackingTools.py3\n")
#    os._exit(1)

# Function Deffinitions
def printProgramInfo():
    author = "*** Kryptic Studios ***"
    program = "*** Tools Tamplete ***"

    print(author)
    print(program)
    
    return

def exitProgram(): # Exit Program Function Deffinition.
    exitCheck = False # If false, the program loops. If true, the program will quit.

    while exitCheck == False: # Checks if exitCheck is false.
        user_exit = input("Would you like to exit? 'Y' for Yes or 'N' for No: ") # User input for exit question.

        if user_exit == "Y" or user_exit == "y" or user_exit == "Yes" or user_exit == "yes": # Checks if the user said yes.
            exitCheck = True # Sets exitCheck to true, so the program can exit.
        elif user_exit == "N" or user_exit == "n" or user_exit == "No" or user_exit == "no": # Checks if the user said no.
            # Reset variables(If needed)

            break # Ends exit while loop
        else:
            print("Invalid Input. Please use 'Y' for Yes or 'N' for No. ") # Error message

    return(exitCheck) # Returns the value of exitCheck for the if statment that determines to exit the program in def main.

# Main Function Deffinition
def main():
    version.CheckVersion()
    printProgramInfo()
    
    while True:
        menu = " 1. Option 1\n 2. Option 2\n 3. Option 3\n 4. Option 4\n 5. Option 5\n"
        print(menu)
        userInput = input("Choose your poision: ")

        if userInput in ["1"]:
            os.system('clear')

            print("Option 1")
            print("\nYou choose option 1.")

        if userInput in ["2"]:
            os.system('clear')

            print("Option 2")
            print("\nYou choose option 2.")

        if userInput in ["3"]:
            os.system('clear')

            print("Option 3")
            print("\nYou choose option 3.")

        if userInput in ["4"]:
            os.system('clear')

            print("Option 4")
            print("\nYou choose option 4.")

        if userInput in ["5"]:
            os.system('clear')

            print("Option 5")
            print("\nYou choose option 5.")

        if exitProgram() == True:
            try:
                exit() # Exit program.
            except:
                break # Ends main while true loop
            






# Call to Main
main()
--Hour Logger Program--

Goal: Program that tracks weekly time worked in hours. User can specify if they would like to look at the current calendar week to see time worked by day, whether they want to add or delete time, or if they'd like to export the current calendar week's time.

System Setup - functions
	
	First, set menu that displays all options (use a function called showMenu)
		
		WILL NEED METHOD TO INPUT TEXT CALENDAR 
	
		Prompt for user to select an option and begin the appropriate process
		
			If input is not one of the four options, prompt for another input
	Second, provide method for user to quit the program or continue using it

MAIN Program Setup

	First, need a while loop to keep the program looping as long as the user wants. This starts with quitProgram initializing to 0 and continues as long as it remains 0, checked at the end of every loop by quit().

	Second, need an if statement to check the user input and perform the desired operation accordingly. These options are as follows:

Option 1: Add Time

	First, ask user to input time (may include option to use current system time later)

Option 2: Remove Time

Option 3: Display current calendar week's time

Option 4: Export current calendar week to text file
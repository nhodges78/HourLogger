Work in progress

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

	First, ask user to input time (may include option to use current system time later). It's simpler to have the user enter hours and minutes separately for time conversion purposes.

		The user inputs need to be typecasted to ints because the input method generates a string. These ints are then used as args in setup for time objects.

		Need a method to check the hour and minute of each input to make sure they are in bounds

	Second, take the user input and convert them to time objects for manipulation and math purposes.

	Third, create method for calculating difference in time out and time in, and use it to make sure that the time entered is chronological and in the same day.

		If not, prompt user to reenter time in and time out.

Option 2: Remove Time

Option 3: Display current calendar week's time

Option 4: Export current calendar week to text file

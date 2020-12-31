#hour logger program

import calendar #for formatting calendar outputs on larger scale
import datetime #for working with time values
import os #for cleaning terminal

#FUNCTIONS

def showMenu(): #display program options and get user input
    print("       Hour Logger v1.0")
    print("-------------------------------")
    print("Please select an option below:")
    print("[1] Add Time")
    print("[2] Remove Time")
    print("[3] Display Current Week's Time")
    print("[4] Export Current Week's Time\n")
    sel = input("=> ")
    if sel<'1' or sel>'4': #make sure input is in bounds
        while sel<'1' or sel>'4':
            sel = input("Invalid input, select 1, 2, 3, or 4 => ")

    return sel

def quit(): #ask if user wants to keep using the program
    print("\nContinue?\t[0] YES [1] NO")
    sel = input("=> ")
    if sel<'0' or sel>'1':
        while sel<'0' or sel>'1':
            sel = input("Invalid input, select 0 or 1 => ")

    return sel

#MAIN

quitProgram = '0' #start while loop

while quitProgram=='0':
    select = showMenu()
    
    if select=='1': #Option 1: Add Time
        print("added time")

    if select=='2': #Option 2: Remove Time
        print("removed time")

    if select=='3': #Option 3: Display current calendar period's time
        print("displaying")

    if select=='4': #Option 4: Export current period to txt
        print("exporting")

    quitProgram = quit()

print("\n\nDone.")
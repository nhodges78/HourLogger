#hour logger program

import calendar #for formatting calendar outputs on larger scale
import datetime #for working with time values
import os #for cleaning terminal

#FUNCTIONS

def showMenu(): #display program options and get user input
    print("       Hour Logger v1.0")
    print("-------------------------------")
    print("Today's Date: " + str(datetime.date.today()))
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

def getTimeIn():
    hourIn = input("\nTime In (HH): ") #get time in and out
    hourIn = int(hourIn)
    if hourIn<00 or hourIn>23:
        while hourIn<00 or hourIn>23:
            hourIn = input("Please enter a number between 00 and 23: ")
            hourIn = int(hourIn)
        
    minIn = input("\nTime In (MM): ")
    minIn = int(minIn)
    if minIn<00 or minIn>59:
        while minIn<00 or minIn>59:
            minIn = input("Please enter a number between 00 and 59: ")
            minIn = int(minIn)

    return datetime.time(hourIn, minIn) #convert to time object

def getTimeOut():
    hourOut = input("\nTime Out (HH): ")
    hourOut = int(hourOut)
    if hourOut<00 or hourOut>23:
        while hourOut<00 or hourOut>23:
            hourOut = input("Please enter a number between 00 and 23: ")
            hourOut = int(hourOut)

    minOut = input("\nTime Out (MM): ")
    minOut = int(minOut)
    if minOut<00 or minOut>59:
        while minOut<00 or minOut>59:
            minOut = input("Please enter a number between 00 and 59: ")
            minOut = int(minOut)

    return datetime.time(hourOut, minOut)

def checkDiff(timeIn, timeOut):
    timeInTD = datetime.timedelta(minutes=timeIn.minute,hours=timeIn.hour)
    timeOutTD = datetime.timedelta(minutes=timeOut.minute,hours=timeOut.hour)
    return timeOutTD-timeInTD

#MAIN

quitProgram = '0' #start while loop

while quitProgram=='0':
    select = showMenu()
    
    if select=='1': #Option 1: Add Time
        print("\n             Add Time               ")
        print("------------------------------------")
        print("Please enter time in 24-hour format.")
        
        timeIn = getTimeIn()
        timeOut = getTimeOut()
        difference = checkDiff(timeIn, timeOut)
        dayCount = int(difference.days)
        if dayCount<0: #negative time difference, prompt correction
            while dayCount<0:
                print("Negative time difference.")
                print("Please input same-day time in and time out in")
                print("24-hour time with time out later than time in.") 
                timeIn = getTimeIn()
                timeOut = getTimeOut()
                difference = checkDiff(timeIn, timeOut)
                dayCount = int(difference.days)

        print(timeIn, timeOut, difference)

    if select=='2': #Option 2: Remove Time
        print("removed time")

    if select=='3': #Option 3: Display current calendar period's time
        print("displaying")

    if select=='4': #Option 4: Export current period to txt
        print("exporting")

    quitProgram = quit()

print("\n\nDone.")
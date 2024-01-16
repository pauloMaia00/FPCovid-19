# Put your name here: Paulo Maia

# Don't change this line:
from datetime import datetime

# Put your program here

def main():
    # Uses while True loop to repeat the program until the user ends it.
    while True:
        # Call banner()
        banner()
        # Call menu()
        numberMenu = menu()
        # Check to see if the value of numberMenu is equal to 1
        if numberMenu == 1:
            # Display a user friendly message
            print('Show menu')
        # Check to see if the value of numberMenu is equal to 2
        elif numberMenu == 2:
            # Call openCDCfile()
            file = openCDCfile()
            # Call defaultReport() and pass the variable file
            defaultReport(file)
            # Display message to let user know the report has been created
            print('Full Mortality Report by State Created')
        # Check to see if the value of numberMenu is equal to 3
        elif numberMenu == 3:
            # Display message
            file = openCDCfile()
            reportSingleStateDataByData(file)
        # Check to see if the value of numberMenu is equal to 4
        elif numberMenu == 4:
            file = openCDCfile()
            getHighestMortality(file)
        # Check to see if the value of numberMenu is equal to 5
        
        elif numberMenu == 5:
            # Display a message stating that the program is ending
            print('Existing Program')
            # Use to break out of the loop
            break
            # If none of the statements above are true, do this instead.
        else:
            # Use to continue the loop
            pass


# Create a function called banner()
# This function will display an ASCII banner
def banner():
    # Assign string to variable bannerDisplay
    bannerDisplay = str('''
 ___                                 
|__  | |\ |  /\  |                   
|    | | \| /~~\ |___                                                 
    __   __   __        ___  __  ___ 
   |__) |__) /  \    | |__  /  `  |  
   |    |  \ \__/ \__/ |___ \__,  |  
                                                               
  ''')
    # Print the banner
    print(bannerDisplay)


# Create a function called menu()
# This function will display option
# Then ask the user to make a selection
# This function will also test the selection to make sure it's value
def menu():
    # Display the menu title
    print('Mortality Rate Comparison Menu')
    print()
    # Display the menu options
    print('1. Show this Menu Again')
    print('2. Full Mortality Report by State')
    print('3. Mortality for a Single State, by Date Range')
    print('4. Highest COVID mortality Week')
    print('5. Exit')
    print()
    # Accepts user input from keyboard, assigns input to variable selection
    selection = input('Make your selection from the menu: ')
    # Use a for loop to test the selection other and other until valid value is selected
    for number in selection:
        #Use try/except statement to test the selection
        try:
            # return if the selection is valid
            return int(selection)

        except:
            # If the selection is not valid, display this message
            # Tell the use to select any character to show the menu
            input(
                'Invalid choose. Select any character to display menu again: ')


# Create a function called openCDCfile()
# This function will open the cdc.csv file
# Also it will remove unneeded lines of data
def openCDCfile():
    # Open the cdc.csv file to read to
    fileHandler = open('cdc.csv', 'r')
    # Use next() to remove unneeded lines of data
    next(fileHandler)
    next(fileHandler)
    next(fileHandler)
    next(fileHandler)
    next(fileHandler)
    next(fileHandler)
    next(fileHandler)
    # Return the fileHandler
    return fileHandler


# Create a function called defaultReport()
# This function will create a report called "Full_Mortaltiy_By_State_Report.txt"
# The report will only show all of the data that is required
def defaultReport(f):
    # Create and open the text file to write on
    fileHandler = open('Full_Moratlity_By_State_Report.txt', 'w')
    # Create headers for the text file
    header1 = 'National Mortality Rate by Cause listed by State and Reporting Date Report    Sorted by State'

    header3 ='States                    Week        Total Causes      Natural Causes    C19 Multiple    C19 Underlying'
    # Write the header1 in the text file
    fileHandler.write(header1)
    # Create a timestamp that automatically generates when the report is written
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y     %H:%M:%S")
    fileHandler.write('\nReport Generated: ' + dt_string + '\n')
    # Write header3 in the textfile
    fileHandler.write(header3 + '\n')

    # Use for loop to write each line of data in the text file
    for each in f:
        # Use each.rstrip() to remove extra lines
        each = each.rstrip()
        # Use each.split() to split up the string in a list
        each = each.split(',')
        # Write the data at index 0,3,4,5,17,and 18 to the report
        # Also use ' '*(x-len(each[x])) to write columns in the report
        fileHandler.write(each[0] + " " * (25 - len(each[0])) + ' ' + each[3] +
                          ' ' * (15 - len(each[3])) + ' ' + each[4] + ' ' *
                          (20 - len(each[5])) + ' ' + each[5] + ' ' *
                          (30 - len(each)) + ' ' + each[17] + ' ' *
                          (15 - len(each[17])) + ' ' + each[18] + '\n')
    # Close the written report
    f.close()


# Ask the user for the start and end dates for the report.
# Gives an automatically setting start and end dates with letter 'S' and 'E'
# Start and end date input requests must repeat individually
# Accept nothing
# Return a valid start and end date as string
def getUserInput():

    first, last = getAvailableDates()

    while True:
        try:
            
            firstChose = convertDate(
                input(
                    'Choose your starting date in (mm/dd/yyyy): '
                ))
            
            lastChose = convertDate(
                input(
                    'Choose your ending date in (mm/dd/yyyy): '
                ))
            break

        except:
            input('Not a vaild date of format. Please try again.')
    pass

    stringFirst = (firstChose.strftime("%m/%d/%Y"))
    stringLast = (lastChose.strftime('%m/%d/%Y'))

    return stringFirst, stringLast


# Determines if the start and end date are available in the document
# Accept nothing
# Returns two strings: start date, and end date
def getAvailableDates():

    cdcFile = openCDCfile()

    openFile = cdcFile.read()
    firstDate = openFile.split(',')[3]
    lastDate = "11/6/2021"

    print('Reporting is available from', firstDate, 'to', lastDate)


    return firstDate, lastDate


#This function reports for a single, user selected state.
# And for a specific, user defined date range.
# Ask user to enter a State to review.
# Using the State and date range, generate a report file called
# "Mortality_For_State_BY_Range_Report.txt"
# Accepts nothing
# Return nothing
def reportSingleStateDataByData(f):

    inputState = input('What State do you want to review? ')

    call = getUserInput()

    fileHandler = open("Mortality_For_State_By_Date_Range_Report.txt", 'w')

    header1 = (
        'Mortality for state by Date Range    For the selected Date range ')

    header3 = '''States                    Week        Total Causes      Natural Causes    C19 Multiple    C19 Underlying '''

    # Write the header1 in the text file
    fileHandler.write(header1)
    # Create a timestamp that automatically generates when the report is written
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y     %H:%M:%S")
    fileHandler.write('\nReport Generated: ' + dt_string + '\n')
    # Write header3 in the textfile
    fileHandler.write(header3 + '\n')

    for each in f:
        each = each.rstrip()
        if each.startswith(inputState):
            each = each.split(',')
            fileHandler.write(each[0] + " " * (25 - len(each[0])) + ' ' +
                              each[3] + ' ' * (15 - len(each[3])) + ' ' +
                              each[4] + ' ' * (20 - len(each[5])) + ' ' +
                              each[5] + ' ' * (30 - len(each)) + ' ' +
                              each[17] + ' ' * (15 - len(each[17])) + ' ' +
                              each[18] + '\n')

    f.close()
    print("***** REPORT PRINTED *****")


# Receives the open file handler, the State, and four integers
# Converts the integers to strings, then appends the summary detail to the report
# Accepts nothing
# Returns nothing
def printLineDetailReport(mS, fh, td, tn, tc, tc2):

    death = str(td)
    natural = str(tn)
    cause = str(tc)
    cause2 = str(tc2)

    fh.write(mS + " " * (25 - len(mS)) + ' ' + death + ' ' *
             (20 - len(death)) + ' ' + natural + ' ' * (30 - len(natural)) +
             ' ' + cause + ' ' * (15 - len(cause)) + ' ' + cause2)


#This function determine the highest reported week of Covid19 mortality as an underlying cause of death
# What week that was, what state it occured in, and what percentage of total deaths that week this number represents
# Accepts nothing
# Returns nothing
def getHighestMortality(f):

    myState = []

    myDate = []

    myCause = []

    for each in f:

        each = each.rstrip()

        each = each.split(',')

        myCause.append(int(replaceSpaceWithZero((each[18]))))
        myState.append(each[0])
        myDate.append(each[3])

    f.close()

    HighestMortality = max(myCause)

    value = myCause.index(HighestMortality)

    week = myDate[value]

    state = myState[value]

    print(
        'The largest number of deaths directly attributible to COVID 19 in this report range was',
        HighestMortality, 'in', state, 'during the week of', week)


# ----------------------------------------------------------------------
# Put all of your code ABOVE this block of code
# This next code block MUST be at the very bottom of your program.
# Leave everthing below this line alone!
# Make no changes below this line!
# --------------------------------

###  HELPER FUNCTION FOR YOU ###


# use this function when you need to compare date strings
# you can't actually compare strings that "look" like dates
# because they aren't date objects. They won't sort like you
# expect them to.
# This function accepts date in mm/dd/yyyy format as a string
# returns date in yy/mm/dd format as a date object (not a string!!!)
def convertDate(dateString):
    objDate = datetime.strptime(dateString, '%m/%d/%Y')
    objDate = objDate.date()
    return objDate


# Recall that you can't perform math functions on empty strings.
# Use this function to replace blank values with zero so that any math will work
def replaceSpaceWithZero(uString):
    if uString == '':
        uString = 0
    return int(uString)


# I've called main() for you.
# This line is a special way to call main
# that allows me to test your code.  Do not change it!
if __name__ == '__main__':
    main()

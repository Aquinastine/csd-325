#Jason Luttrell 12/17/24  CSD205-T301 Module 4.2 Miles to Kilometers converter
#This scrypt converts miles to kilometers.

#Success Criteria:
#1. Write a program that uses a function to convert miles to kilometers. 
#2. Your program should prompt the user for the number of miles driven
#3. call a function which converts miles to kilometers. 
#4. Check and validate all user input and incorporate Try/Except block(s). 
#5. The program should then display the total miles and the kilometers.

def Main():
    WelcomeMsg()
    lsMiles = Conversion('of Miles Driven')
    if lsMiles == False: pass
    else:
        OutputConversion(lsMiles)


def WelcomeMsg():
    #Initialize some message strings used in the script and publish the welcome message
    stCompanyNm = 'Acme Engineering Applications Inc' #Company Name will be reused
    #Build the welcome Message
    stWelcomeMsg = 'You have initiated the SuperWamodyne Miles to Kilometer Converter (SWMKC)! \n' + \
                    'This application is brought to you by '+ stCompanyNm +'\n' + \
                    'It will calculate the kilometers driven based on miles driven!...\n'   
    print(stWelcomeMsg) #Print Welcome Message

def Conversion(inputdescription):
    # Get valid inputs from the user and make the conversion to kilometers
    flInput = input(F'Please enter the number {inputdescription}? ') #Get input
    flKm = lambda a : a * 1.609344 #Define the converstion function
    try:
        flResult = flKm(float(flInput)) #execute the conversion function
    except: #If the user input a non number, then raise the error and get another input
        print('You entered something that either isn\'t a number. Rerun the program to try again.') #raise the error
        return False #return false to indicate an invalid input
    return [float(flInput), flResult]

def OutputConversion(Conversion):
    #output the result in a message to the user
    print(f'{Conversion[0]:,.2f} miles driven is equal to {Conversion[1]:,.2f} kilometers.')

Main()
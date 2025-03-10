#Jason Luttrell 3/9/25  CSD325-T301 Module 10.2 Inheritance
#This scrypt will all the lyrics to the 100 bottles of beer song
#starting at the number provided by the user

#Success Criteria:
#1. Ask the user how many bottles of beer are on the wall.
#2. Pass that input to a function that manages the countdown.
#3. The function should take the input and count backwards to 1 while 
#   displaying the number of remaining bottles of beer on the wall.
#4. Once the count is down to 1, change lyrics to show "1 bottle of 
#   beer..."
#5. At the end of the countdown, get back to the main program and remind 
#   the user to buy more beer.


def main():

    #singSong will produce the lyrics based on the user input from 
    #getPosInt()
    singSong(getPosInt())


#Function gets the number of bottles on the wall from the user
def getPosInt():
    import math #Importing a function to round up
    
    tryAgain = True #Set a sentinel variable for the while loop
    
    #The loop will allow the user to keep trying to put a 
    # number of bottles in until they input something that makes 
    # sense.
    while tryAgain:
            
            #Create the try again message
            tryAgainMsg ='\nType "y" to try again, otherwise type any ' \
                + 'character: '
            #Create the error message
            errMsg = '\nThat wasn\'t a number greater than zero!'
            
            #Putting the inside of the loop in a try-except statement to 
            # handle any non-numeric inputs, without exiting the loop
            try:
                #Define the input message
                inputMsg = 'Please input the number of beer bottles ' \
                    + 'on the wall: '
                
                #Get the input, convert the text to a float and round up.
                #Partial bottles of beer deserve to be drunk too.
                #Once the float is rounded it is converted to an integer.
                # If this errors it is because the input is not numeric
                n = int(math.ceil(float(input(inputMsg))))
                
                #Check to make sure the  input is greater than 0
                if n > 0: return n
                else:
                    #print an error message
                    print(errMsg)
                    #let the person try again
                    if input(tryAgainMsg).lower() != 'y':
                        tryAgain = False
            
            except:
                #print an error message
                print(errMsg)
                #let the person try again
                if input(tryAgainMsg).lower() != 'y':
                    tryAgain = False
    if not tryAgain: exit

#This function produces the song lyrics based on the number of bottles
def singSong(n):
    #Run the while loop until the n goes to zero
    while n > 0:
        #If n is greater than 2, print the verse for >2 bottles
        if n > 2: print(f'\n{n} bottles of beer on the wall, {n} bottles of ' \
        f'beer. \n Take one down, pass it around, {n-1} bottles of beer ' \
        'on the wall.\n\n')
        #If n = 2, print the verse for 2 bottles
        elif n == 2: print(f'{n} bottles of beer on the wall, {n} bottles of ' \
        f'beer. \n Take one down, pass it around, {n-1} bottle of beer ' \
        'on the wall.\n\n')
        #otherwise (the only option is 1), print the verse for 1 bottle
        else: 
            print(f'{n} bottle of beer on the wall, {n} bottle of ' \
        f'beer. \n Take one down, pass it around, {n-1} bottles of beer ' \
        'on the wall.\n\n')
        #subtract 1 bottle from the wall
        n -= 1
    
    print("\n Time to buy more beer!\n")
    


if __name__ == "__main__":
    main()
    
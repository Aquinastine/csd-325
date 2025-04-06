import csv
from datetime import datetime
import os
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import sys

def main():
    #Get the current path of the script:
    #Assuming the .csv file is in the same directory as this .py file, this
    #will allow the user to access the .csv file without changing the working
    #directory or updating the script.
    path = os.path.abspath(__file__) #returns the path+filename
    path = path[:path.rfind('\\')+1]#strips the filename

    filename = path +'sitka_weather_2018_simple.csv'
    
    # Set exit variable
    global Exit
    Exit = False

    #launch Menu
    while not Exit:
        displayMenuItems(filename)
    
    



#Define a function to get the user input (uses Matplotlib as a GUI)
def displayMenuItems(filename):

    # Create an empty figure
    fig_menu= plt.figure (figsize=(1,1))
    #plt.subplots_adjust(bottom=0.2)  # Adjust the bottom to make space for the button

    # Add a buttons
    # Define the button's position and size [left, bottom, width, height]
    button1_ax = plt.axes([0.1, 0.8, 0.5, 0.2])
    button1 = Button(button1_ax, 'Click To View Historical Highs')
    
    button2_ax = plt.axes([0.1, 0.5, 0.5, 0.2])
    button2 = Button(button2_ax, 'Click To View Historical Lows')

    button3_ax = plt.axes([0.1, 0.2, 0.5, 0.2])
    button3 = Button(button3_ax, 'Click To Exit')
    
    button1.on_clicked(lambda event:on_button_click(filename, parameter="high"))
    button2.on_clicked(lambda event:on_button_click(filename, parameter="low"))
    button3.on_clicked(lambda event:on_button_click(filename, parameter="exit"))

    # Display the figure
    plt.show()

# Define a callback function for button click
def on_button_click(filename, parameter):
    if parameter == 'exit': 
        exitMsg()
    elif parameter == 'high':
        dataLists = buildlist(filename,parameter)
        plotGraph(filename,parameter,dataLists[0],dataLists[1])
        
    else:
        dataLists = buildlist(filename,parameter)
        plotGraph(filename, parameter,dataLists[0],dataLists[1])
        
    
#Given the filename, builds the list. Parameter must be "high" or "low"
#The function returns of list of 2 lists, [0] is list of the dates. 
# [1] is the parameters specified in the parameter arguement.
def buildlist(filename, parameter): 
    #Choose the approppriate parameter row and save it.
    if parameter == 'high': param_row = 5
    else: param_row = 6
       
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and parameter temperatures from the .csv file.
        dates, params = [], []
        for row in reader:
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
            params.append(int(row[param_row]))

    #Return the lists
    return([dates,params])

#plots a graph of the selected parameters. Arguments are:
#parameter - high or low, based on user selection
#dates - list of dates for each row in the .csv
#params - list of either high or low temps for each date
def plotGraph(filename, parameter, dates, params,):
    #Close any existing plots
    plt.close()
    
    #get the param variables
    color, altParam = setParamVariables(parameter)
    
    #Create the plot
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(dates, params, c=color)
    plt.subplots_adjust(bottom=.25)

    # Format plot.
    ax.set_title(f"Daily {parameter.capitalize()} Temperatures - 2018", 
                 fontsize=24)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    fig.autofmt_xdate()
    

    
    plt.show()

# Select the color based on the parameter, and define the alternate
# parameter for the button functionality    
def setParamVariables(parameter):
    if parameter == 'high': 
        color = 'red'
        altParam = 'low'
    else: 
        color = 'blue'
        altParam = 'high'
    return([color,altParam])

#Redraws the plot based on the parameter passed     
def switchGraph(filename, parameter):
    dates, params = buildlist(filename, parameter)
    plotGraph(filename, parameter, dates, params)
    
def exitMsg():
    # close any existing plots
    plt.close()
    global Exit 
    Exit = True
    # Create an empty figure
    fig = plt.figure(figsize=(2, 1))
    plt.text(0.1, 0.5, "Goodbye!", fontsize=14)
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
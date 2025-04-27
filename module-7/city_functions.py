#Luttrell, Jason Module 6.2 City Functions
#Displays a city and country once the city and countries are input 

import csv
import os

def main():
    #Get the current path of the script:
    #Assuming the .csv file is in the same directory as this .py file, this
    #will allow the user to access the .csv file without changing the working
    #directory or updating the script.
    path = os.path.abspath(__file__) #returns the path+filename of the script
    path = path[:path.rfind('\\')+1]#strips the filename

    #Adds the filename of the cities.csv file onto path
    filename = path +'cities.csv'
        
    #Open the file, create a reader and save it as a list
    #This will make a list of rows as strings e.g. 'city,country'
    citiesLst = list(csv.reader(open(filename, 'r')))
     
    #loop through each item in the list    
    for rows in citiesLst:
        print (displayCityCountry(List=rows))
    
    



#Define a function to display the City and Country to Console
#either city and country need to be entered as individual arguments or
#a list with [City,Country] is needed. If both are provided then the city
#and country arguments will be used.
def displayCityCountry(City='',Country='',Population='',language='',List=''):
    #If there is only a country and city argument
    if City and Country and not Population:
        string = f'{City}, {Country}'
        return string.title()
    
    #if there is city country and population
    if City and Country and Population:
        string = f'{City}, {Country} - population {Population}'
    
    #if there is city country, population and language
    if City and Country and Population and language:
        string = f'{City}, {Country} - population {Population}, {language}'
    
    #if there is a list with exactly 2 arguments
    elif List and len(List) == 2:
        string = f'{List[0]}, {List[1]}'
        return string.title()
    
    #if there is a list with exactly 3 arguments
    elif List and len(List) == 3:
        string = f'{List[0]}, {List[1]} - population {List[2]}'
        return string.title()
    
    #if there is a list with exactly 4 arguments
    elif List and len(List) == 4:
        string = f'{List[0]}, {List[1]} - population {List[2]}, {List[3]}'
        return string.title()    
      
    else:
         return 'there is a problem with the inputs'


if __name__ == "__main__":
    main()
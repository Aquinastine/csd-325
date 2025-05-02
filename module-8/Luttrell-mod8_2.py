#Luttrell, Jason Module 6.2 City Functions
#Displays a list of student from the JSON file and then adds a name to the
#file, then give the user the option to save it

import json
import os

# Main program
def main():
     #Get the current path of the script:
    #Assuming the .csv file is in the same directory as this .py file, this
    #will allow the user to access the .csv file without changing the working
    #directory or updating the script.
    path = os.path.abspath(__file__) #returns the path+filename of the script
    path = path[:path.rfind('\\')+1]#strips the filename

    #Adds the filename of the cities.csv file onto path
    filename = path +'students.json'

    # Load and show original list
    students = load_students(filename) #Save JSON File Object
    print("Original Student List:")
    print_students(students) #Print JSON File Object

    # Append myself as a new student
    new_student = {
        "F_Name": "Jason",
        "L_Name": "Luttrell",
        "Student_ID": 99999,
        "Email": "jluttrell@my365.bellevue.edu"
    }
    students.append(new_student)

    # Show updated list
    print("\nUpdated Student List:")
    print_students(students)

    # Save back to JSON file
    save_students(filename, students)


# Load JSON data into Python list
def load_students(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Print formatted student data
def print_students(student_list):
    for student in student_list:
        string = f"{student['L_Name']},{student['F_Name']} " \
        + f": ID = {student['Student_ID']} , Email = {student['Email']}"
        print(string)

# Save updated list back to JSON
def save_students(filename, student_list):
    with open(filename, 'w') as file:
        json.dump(student_list, file, indent=2)
    
    print("\nThe student.json file has been updated.")


if __name__ == "__main__":
    main()
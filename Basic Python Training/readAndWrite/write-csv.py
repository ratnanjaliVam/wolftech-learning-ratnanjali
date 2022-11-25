# Program to write in a csv file using Python

# To read or write in csv, we have to import the csv module in python.
import csv

# Opening the file in which the data is to be written, if there is no file, then it will create one csv file to write
with open('assets/employeeDetails.csv', 'w') as f:

    # The writer method allows us to write in the csv file.
    data = csv.writer(f)

    # Here, I am taking the example to write employee details in a csv file.
    name = input("Employee Name: ")
    age = input("Employee Age: ")
    designation = input("Employee Designation: ")

    # writerow method appends a row in csv, it takes only one argument
    # but here I have used three fields so I am giving the argument as a list
    data.writerow([name, age, designation])





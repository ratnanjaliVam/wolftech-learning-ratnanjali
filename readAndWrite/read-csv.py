# Program to Read a csv file using Python

# To read or write in csv, we have to import the csv module in python.
import csv

# Opening the csv file which is to be read.
with open("assets/detail.csv", "r") as f:

    # Using the reader method of csv module to read the file.
    data = csv.reader(f)

    # Parsing through the data and printing each object of the csv file.
    for i in data:
        print(i)
# end
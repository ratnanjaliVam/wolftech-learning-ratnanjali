# Program to read a TEXT file in Python

# Using the open module to open the file which is to be read.
file1 = open('assets/aboutme.txt')

# read module allows to parse through the given file
readingFile = file1.read()

# Printing the contents of the file which is read.
print(readingFile)
file1.close()


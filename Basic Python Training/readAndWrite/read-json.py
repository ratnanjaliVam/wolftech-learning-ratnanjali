# Program to Read a JSON file using Python

# To read or write in JSON, we have to import the json module in python.
import json

# When we open any file using the open function, it reads the data in the form of string.
newFile = json.load(open("assets/info.json"))

# loads is used when we want to convert string to json
# load is used when we want to convert any file to json

print("json goes here!!!")
print(newFile)


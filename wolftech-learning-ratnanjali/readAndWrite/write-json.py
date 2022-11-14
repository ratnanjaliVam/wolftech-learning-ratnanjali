# Program to Read a JSON file using Python

# To read or write in JSON, we have to import the json module in python.
import json

# Using the open() function to go to the file in which the data is to be written.
# It can create a new file if the file doesn't exist
infoText = open("assets/info.json")

# load is used when we want to convert any file to json
fileDict = json.load(infoText)

# As the json file contains key and values, therefore, appending the dictionary
fileDict["age"] = "21"
fileDict["passout"] = "2022"


# We can also delete any key in json file using the pop() function.
# deleting any key with value from the dictionary
fileDict.pop('age')

print(fileDict)

# appending dictionary after deleting
json.dump(fileDict, open("assets/info.json", "w"))

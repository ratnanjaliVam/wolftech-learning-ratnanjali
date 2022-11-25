import pandas as pd
my_dictionary = {"names":["rohan", "mohan","sohan"], "hindi":[40, 41, 42], "english" : [40, 45, 50]}


df1 = pd.DataFrame(my_dictionary)
df1["total"] = df1["hindi"] + df1["english"]
df1["pecentage"] = [str(x) + "%" for x in df1["total"]]

new_dictionary = {"names":["rohani", "mohani","sohani"], "hindi":[40, 41, 42], "english" : [40, 45, 50]}
df2 = pd.DataFrame(new_dictionary)
df2["total"] = df2["hindi"] + df2["english"]
df2["pecentage"] = [str(x) + "%" for x in df2["total"]]

df3 = pd.concat([df1,df2], ignore_index=True)
print(df3)
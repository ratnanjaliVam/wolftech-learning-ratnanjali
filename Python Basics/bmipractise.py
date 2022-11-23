import pandas as pd

my_dictionary = {"names":["ritu", "mitu", "situ"], "weight":[40, 41, 42], "height" : [40, 45, 50]}

df = pd.DataFrame(my_dictionary)
df["BMI"] = [x/(y**2) for x,y in zip(df["weight"],df["height"])]
print(df)

new_dictionary = {"names":["ritu", "mitu", "situ"], "age":[40, 41, 42], "income" : [4000, 4500, 5000]}
df1 = pd.DataFrame(new_dictionary)

df3 = pd.concat()
print(df1)
import pandas as pd

list = {
    "Name":['Ram','shayam','Mohan','Delhi'],
    "Age":[20,30,40,50],
    "City":['Delhi','Mumbai','Lucknow','Bhopal']
}

df = pd.DataFrame(list)
# df.to_csv("Output.csv" , index=False)
# df.to_excel("Output.xlsx" , index=False)
df.to_json("output.json",index=False)
# print(df)
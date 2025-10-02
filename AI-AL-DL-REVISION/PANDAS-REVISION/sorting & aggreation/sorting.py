# sorting data
# sorting data 1 column sort_values()
# df.sort_values(by="column_name",True/False,inplace=True)

import pandas as pd

data = {
    "Name":['Arun','Varun','Karun'],
    "Age":[10,20,8],
    "Salary":[10000,20000,30000]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by="Age" , ascending=True , inplace=True)
print("Sorted age by ascending")
print(df)
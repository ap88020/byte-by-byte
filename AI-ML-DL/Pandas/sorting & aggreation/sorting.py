# Sorting
# Sorting data in one column sort_values()
# df.sort_values(by="Columns Name",True/False , inplace=True)

import pandas as pd

data = {
    "Name":['Arun','Varun','Karun'],
    "Age":[33,22,66],
    "Sallary":[20000,30000,40000]
}

df = pd.DataFrame(data)

print("-------Sorted Age by Descending--------")
df.sort_values(by="Age",ascending=False,inplace=True)
print(df)


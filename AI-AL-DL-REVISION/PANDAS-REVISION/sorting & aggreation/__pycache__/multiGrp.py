import pandas as pd

data = {
    "Name":['Arun','Varun','Tarun','Marun','Karun'],
    "Age":[20,28,32,21,28       ],
    "Salary":[50000,60000,45000,52000,48000]
}


df = pd.DataFrame(data)
groupd = df.groupby(["Age","Name"])["Salary"].sum()

print(groupd)

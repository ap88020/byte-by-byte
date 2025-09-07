import pandas as pd

data = {
    "Name": ['Arun','Varun','Karun','Tarun','Sarun'],
    "Age": [33,22,22,99,18],
    "Salary": [53000,22000,42000,34000,43000]
}

df = pd.DataFrame(data)

grouped = df.groupby(["Age","Name"])["Salary"].sum()

print(grouped)


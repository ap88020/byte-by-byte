"""
1- how big you dataseet
2- what are names of columns

shape columns
"""

import pandas as pd

data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Kirti','Shruti','Murti'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}
df = pd.DataFrame(data)

print(df)
print(f'shape {df.shape}')
print(f'columns {df.columns}')
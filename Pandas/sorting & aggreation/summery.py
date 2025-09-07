"""
df["columns_name"].mean()
df["columns_name"].sum()
df["columns_name"].min()
df["columns_name"].max()
"""

import pandas as pd
data = {
    "Name":['Arun','Varun','Karun'],
    "Age":[33,22,66],
    "Sallary":[20000,30000,40000]
}

df = pd.DataFrame(data)

average_sallary = df['Sallary'].mean()
total_sallary = df['Sallary'].sum()
minimum_sallary = df['Sallary'].min()
max_sallary = df['Sallary'].max()

print(f"Average sallary -> {average_sallary}")
print(f"Total Sallary -> {total_sallary}")
print(f"Minumum Sallary -> {minimum_sallary}")
print(f"Max Sallary -> {max_sallary}")
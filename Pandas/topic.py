"""
1-> how big your dataseet
2-> what are the names of columns

shape and columns
"""
import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam','Mohan','Raju','Simran','Jadish'],
    "Age": [20,39,26,42,31,21,32],
    "Sallary": [60000,70000,500000,900000,300000,400000,50000],
    "Performance Score": [90,88,98,78,80,90,89],
}

df = pd.DataFrame(data)
print(df)
print("printing shape or columns") 

print(f"columsn : {df.columns}")
print(f"shape : {df.shape}")
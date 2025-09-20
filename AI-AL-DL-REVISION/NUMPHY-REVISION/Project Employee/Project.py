import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\91838\Documents\byte_by_byte\AI-AL-DL-REVISION\NUMPHY-REVISION\Project Employee\employee_data_sheet.csv")

# print(df)

print("Missing value in each dataSheet")

print(df.isnull().sum())

df['Salary (INR)'].fillna(df['Salary (INR)'].mean(),inplace=True) 
df['Performance Rating'].fillna(df['Performance Rating'].median(),inplace=True)

df.replace([np.nan , -np.nan],np.nan,inplace=True)

df.fillna(df.mean(),inplace=True) 

df.drop_duplicates(inplace=True)

df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0 , df['Salary (INR)'].mean(),df['Salary (INR)'])


salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()

print(df)

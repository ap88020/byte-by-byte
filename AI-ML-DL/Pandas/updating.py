import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam','Mohan','Raju','Simran','Jadish'],
    "Age": [20,39,26,42,31,21,32],
    "Sallary": [60000,70000,500000,900000,300000,400000,50000],
    "Performance Score": [90,88,98,78,80,90,89],
}



df = pd.DataFrame(data)

# METHOD----------1
# df.loc[0,'Sallary'] = 65000

# print(df)

# METHOD------------2
# Increasing sallary with 5 percent
df['Sallary'] = df['Sallary'] * 1.05
print(df)
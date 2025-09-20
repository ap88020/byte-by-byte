import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam','Mohan','Raju','Simran','Jadish'],
    "Age": [20,None,26,42,31,21,32],
    "Sallary": [60000,None,500000,900000,300000,400000,50000],
    "Performance Score": [90,None,98,78,80,90,89],
}


df = pd.DataFrame(data)

# print(df.isnull().sum())
# print(df.isnull())


# method-> linear , polynomial , time

df.interpolate(method='linear', axis=0, inplace=True)
print(df)
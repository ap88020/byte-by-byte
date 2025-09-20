import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam','Mohan','Raju','Simran','Jadish'],
    "Age": [20,39,26,42,31,21,32],
    "Sallary": [60000,70000,500000,900000,300000,400000,50000],
    "Performance Score": [90,88,98,78,80,90,89],
}

df = pd.DataFrame(data)

# df.drope(columns = ["columns_name"],inplace=true)
df.drop(columns=["Performance Score","Age"],inplace=True)

print(df)
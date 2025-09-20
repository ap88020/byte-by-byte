# fillna()
# fillna(value,inplace=true)
import pandas as pd

# dropna


data = {
    "Name": ['Ram',None,'Ghanshyam','Mohan','Raju','Simran','Jadish'],
    "Age": [20,None,26,42,31,21,32],
    "Sallary": [60000,None,500000,900000,300000,400000,50000],
    "Performance Score": [90,None,98,78,80,90,89],
}


df = pd.DataFrame(data)
print(df)

# print("----------After droping------------")
# df.dropna(inplace=True)
# print(df)

print("----------Fill Na------------")

df.fillna(0,inplace=True)

print(df)

print("----------mean value------------")
# df['Age'] = df.fillna(df['Age'].mean(),inplace=True)
# df['Sallary'].fillna(df['Sallary'].mean())

df.fillna({
    "Age": df['Age'].mean(),
    "Sallary": df['Sallary'].mean(),
    "Performance Score": df['Performance Score'].mean()
}, inplace=True)


print(df)
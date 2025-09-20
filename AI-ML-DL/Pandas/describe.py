import pandas as dp

data = {
    "Name": ['Ram','Shyam','Ghanshyam','Mohan','Raju','Simran','Jadish'],
    "Age": [20,39,26,42,31,21,32],
    "Sallary": [60000,70000,500000,900000,300000,400000,50000],
    "Performance Score": [90,88,98,78,80,90,89],
}

df = dp.DataFrame(data)

print("Sample Data-Frame")
print(df)

print("Descriptive Statistic")
print(df.describe())
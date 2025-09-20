import pandas as dp

data = {
    "Name": ['Ram','Shyam','Ghanshyam','Mohan','Raju','Simran','Jadish'],
    "Age": [20,39,26,42,31,21,32],
    "Sallary": [60000,70000,500000,900000,300000,400000,50000],
    "Performance_Score": [90,88,98,78,80,90,89],
}

df = dp.DataFrame(data)

# high_sallary = df[df['Sallary'] > 400000]
# print("Employees with sallary above 60000")
# print(high_sallary)

# print("employee with sallary above 300000 and age above 31")
# emp = df[(df["Sallary"] > 300000) & (df["Age"]>31)]

# print(emp)

emp_or = df[(df["Age"] > 50) | (df["Performance_Score"] > 90)]
print("employee with age older then 50 or Performance_Score > 80")

print(emp_or)
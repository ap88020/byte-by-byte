import pandas as dp

df = dp.read_csv("sample_empoyee.csv")

print("starting rows")
print(df.head(5))

print("ending 10 rows")
print(df.tail(5))
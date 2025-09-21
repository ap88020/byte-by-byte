import pandas as pd

# df = pd.read_csv("sales_data_sample.csv",encoding="utf-8")
# df = pd.read_excel("sample_employees.xlsx")
df = pd.read_json("sample_Data.json")
print(df)
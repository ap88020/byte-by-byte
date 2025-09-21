import pandas as pd

df = pd.read_csv("sales_data_sample.csv")

print("print 5 first rows of datasheet")
print(df.head(5))

print("Print 5 last rows of datasheets ")
print(df.tail(5))
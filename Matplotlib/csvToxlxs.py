import pandas as pd

df = pd.read_csv('netflix_titles.csv')
# print(df)

df = df.dropna(subset=['type'])
type_counts = df['type'].value_counts()
print(type_counts.index)
print(type_counts.values)
# print(type_counts.values)


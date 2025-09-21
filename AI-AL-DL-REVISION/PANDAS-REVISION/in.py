import pandas as pd

df = pd.read_json("output.json")

print("print josn dataseet info()")

print(df.info())
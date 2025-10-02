import pandas as pd

deta = {
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}

df = pd.DataFrame(deta)

print("====Before Interpolation=====")
print(df)

print("======After Interpolation======") 
df['Value'] = df['Value'].interpolate(method="linear")
print(df)

"""
1-Time series Data
2- numeric Data with trends
3- avoid droping rows
"""
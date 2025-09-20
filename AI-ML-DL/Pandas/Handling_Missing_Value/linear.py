import pandas as dp

data = {
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}

df = dp.DataFrame(data)

print("----------Before Interpolate-----------")
print(df)
# print("----------After Interpolate-----------")
# df['Value'] = df['Value'].interpolate(method="linear")
print("----------After Interpolate with Time-----------")
df['Value'] = df['Value'].interpolate(method="Time")

print(df)
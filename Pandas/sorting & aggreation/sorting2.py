import pandas as pd

data = {
    "Name":['Arun','Varun','Karun'],
    "Age":[33,22,66],
    "Sallary":[20000,30000,40000]
}

df = pd.DataFrame(data)

print("-------Sorted Age OR Sallary by Descending--------")
# df.sort_values(by="Age",ascending=False,inplace=True)
# print(df)

df.sort_values(by=['Age','Sallary'],ascending=[True,True],inplace=True)
print(df)
import pandas as pd

df_customers = pd.DataFrame({
    'CustomerId':[1,2,3],
    'Name':['Ramesh','Suresh','Kalpesh']
})

df_customers1 = pd.DataFrame({
    'CustomerId':[1,2,4],
    'OrderAmount':[250,450,350]
})

df_merged = pd.merge(df_customers,df_customers1,on="CustomerId", how="outer")

print(df_merged)

# df.merge(df1,df2,on="column_name, how="type of joining")

import pandas as pd

# customer dataFrame
df_customers = pd.DataFrame({
    'CustomerId':[1,2,3],
    'CustomerName':['Ramesh','Suresh','Kalpesh']
})

# order dataFrame
df_orders = pd.DataFrame({
    'CustomerId':[1,2,4],
    'OrderAmount':[101,201,301]  
})


# merge

# df_merge = pd.merge(df_customers,df_orders,on="CustomerId",how="inner")

# print("Inner join")
# print(df_merge)
df_merge = pd.merge(df_customers,df_orders,on="CustomerId",how="outer")

print("Outere join")
print(df_merge)
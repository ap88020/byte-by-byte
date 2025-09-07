"""
vertically (row-wise)
horizontally (column-wise)

pd.concate([df1,df2],axios=0,ignore_index=True)

[df1,df2] =
axis = 1
ignore_index = True
"""
import pandas as pd

# Region1
df_region1 = pd.DataFrame({
    'Customer_id':[1,2],
    'CustomerName':['Gopal','Raju']
})

# Region2
df_region2 = pd.DataFrame({
    'Customer_id':[3,4],
    'CustomerName':['Shayam','Baburao']
})

# concatenate vertically
# df_concate = pd.concat([df_region1,df_region2],ignore_index=True)
# print(df_concate)

#concatenate horizontally 
df_concate = pd.concat([df_region1,df_region2],axis=1,ignore_index=True)
print(df_concate)
# pd.merge(df1,df2, on
#      = "column_Name", how = "type of join")

import pandas as pd
from numpy.ma.core import inner

# customer dataframe
df_customer = pd.DataFrame({
     'customerID':[1,2,3],
     'Name':['ramesh','suresh','depesh']
})

# order dataframe

df_orders = pd.DataFrame({
    'customerID':[1,2,4],
    'orderAmount':[250,450,350]

})
# 4 types joint inner join, right join,outer join,left join
df_merged = pd.merge(df_customer,df_orders, on = "customerID", how = "right")
print('right join')
print(df_merged)

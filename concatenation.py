"""
concatenation ka matlab hota hai data ko vertically ya horizontally combine karna

vertically (row-wise)
horizontally (column wise)

pd.concat([df1 , df2],axis = 0 , ignore_index = True)

[df1,df2] =
axis = 1

ignore_index = True

"""
import pandas as pd

# regional
df_Region1 = pd.DataFrame({
    'customerID':[1,2],
    'Name':['Gopal','raju']

})
df_Region2 = pd.DataFrame({
    'customerID':[3,4],
    'Name':['shyam','baburao']
})

df_concat = pd.concat([df_Region1,df_Region2], axis=1, ignore_index= True)
print(df_concat)
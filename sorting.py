#sorting data

# sorting ka ham use
# jaise ki A vale ak sath aajaye alphbet ki tarah

# Sorting data 1 column sort_values()
#df.sort_values(by="column Name",True/False, inplace = True)

import pandas as pd

data = {

    "name":['arun','varun','karun'],
    "age":[12,34,18],
    'salary':[10000,34000,80000]

}
df = pd.DataFrame(data)
df.sort_values(by="age",ascending=True,inplace=True)
print('sorted age by descending')
print(df)

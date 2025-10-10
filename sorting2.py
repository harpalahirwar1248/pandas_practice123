# aab ham multiple column par sorting perform

# df.sort_values(by=['age','salary'],
# ascending = True ,inplace=True)

import pandas as pd

data = {

    "name":['arun','varun','karun'],
    "age":[12,34,18],
    'salary':[10000,34000,80000]

}
df = pd.DataFrame(data)
df.sort_values(by=['age','salary'],ascending=True,inplace=True)
print("sorting age by descending")
print(df)
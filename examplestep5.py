import pandas as np
import pandas as pd

data = {
    "name":["ram","shiva","satya","aryan","divya"],
    "age":[22,19,22,20,19],
    "salary":[30000,20000,35000,100000,70000],
    "performance scores":[50,60,70,87,80]
}
df = pd.DataFrame(data)
print("sample Dataframe")
print(df)

print("name (single column return series)")
Name = df['name']
print(Name)
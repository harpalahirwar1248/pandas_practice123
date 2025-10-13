import pandas as pd

data = {

    "name":['arun','varun','karun','vijay','satya'],
    "age":[12,34,18,21,22],
    "salary":[10000,34000,80000,34000,120000]

}
df = pd.DataFrame(data)
grouped = df.groupby("age")["salary"].sum()
print(grouped)
import pandas as pd


data = {
    "name":["siva","vijay",'satya','aryan',None,'divya'],
    "age":[12,34,9,21,None,19],
    "salary":[10000,50000,29999,700000,None,4000],
    "performance":[10,50,80,85,None,30]
}
df = pd.DataFrame(data)
print(df)
# linear,polynomial,time

df.interpolate(method="linear",axis=0,inplace=True)
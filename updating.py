import pandas as pd
data = {
    "name":["ram","aryan","vijay","satya","raj","shiva","shuvam","divya","shivam","shivani","deep","harpal"],
    "age":[21,20,24,19,23,12,16,15,30,29,26,28],
    "salary":[40000,70000,100000,20000,60000,45000,90000,80000,87000,47000,540000,78000],
    "performance_score":[40,70,100,20,60,45,90,80,87,47,54,78]
}

df = pd.DataFrame(data)
print(df)

# loc[]
# df.loc[row_index,"column Name"]= new value
df.loc[1,"salary"]=1900
print(df)

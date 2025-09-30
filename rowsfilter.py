import pandas as pd

data = {
    "name":["shiva","aryan","vijay","satya"],
    "age":[11,20,21,23],
    "salary":[100000,500000,34000,123000]
}
df = pd.DataFrame(data)
print(df)
high_salary = df[df['salary']>50000]
print("Employees with salary>50000")
print(high_salary)

high_salary = df[df['salary']>100000]
print("employees the salary > 100000")
print(high_salary)

# filtering rows salary > 50k & age > 20

filtered = df[(df['salary']>100000) & (df["age"]>20)]
print(filtered)

filter_or = df[(df['salary']>100000) | (df["age"]>20)]
print(filter_or)

"""
df["column Name"].mean()
df["column Name"].sum()
df["column Name"].min()


"""
import pandas as pd

data = {
    "name":['ram','shiva','aryan','satya'],
    "age":[12,34,56,19],
    "salary":[20000,40000,60000,80000]
}
df = pd.DataFrame(data)
avg_salary = df['salary'].mean()
print(avg_salary)